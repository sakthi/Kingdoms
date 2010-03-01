"""The base Controller API
Provides the BaseController class for subclassing.
"""
import random
import logging
import datetime
import os
import json
import sys
import warnings
import formencode

from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons import config, request, response, session, tmpl_context as c
from kingdoms.lib.helpers import get_token, parse_token
from kingdoms.model import meta, Player
from paste.deploy.converters import aslist
from pylons.controllers.util import abort
from decorator import decorator
from formencode import api, htmlfill, variabledecode
from webob import UnicodeMultiDict

from pylons.decorators.util import get_pylons
from pylons.i18n import _ as pylons_gettext
from kingdoms.lib import object_encoder

log = logging.getLogger(__name__)


def jsonify(func, *args, **kwargs):
	pylons = get_pylons(args)
	pylons.response.headers['Content-Type'] = 'application/json'
	data = func(*args, **kwargs)
	if isinstance(data, (list, tuple)):
		msg = "JSON responses with Array envelopes are susceptible to " \
			  "cross-site data leak attacks, see " \
			  "http://pylonshq.com/warnings/JSONArray"
		warnings.warn(msg, Warning, 2)
		log.warning(msg)
	log.debug("Returning JSON wrapped action output")
	return json.dumps(data, default = object_encoder)
jsonify = decorator(jsonify)


class BaseController(WSGIController):

	def __call__(self, environ, start_response):
		"""Invoke the Controller"""
		# WSGIController.__call__ dispatches to the Controller method
		# the request is routed to. This routing information is
		# available in environ['pylons.routes_dict']
		try:
			cdir = os.path.join(config['kingdoms.data'], 'controls', 'interface', 'corners')
			interface_corners = os.listdir(cdir)
			c.corner = interface_corners[random.randint(0, len(interface_corners) - 1)]
			return WSGIController.__call__(self, environ, start_response)
		finally:
			meta.Session.remove()
			
	def check_auth(self):
		token = get_token()
		if not token:
			log.error('%s token received' % token)
			abort(401)
		id, timestamp = parse_token(token)
		delta = datetime.datetime.now() - datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
		if delta.seconds > 3600:
			log.info('timestamp is too old...')
			abort(401)
		#set user_name to real name
		c.player = meta.Session.query(Player).filter(Player.id == id).one()
		log.debug('user %s passed challange of times.' % c.player)
		return id, timestamp

	def __before__(self):
		#set user info
		c.is_authorized = False
		c.user_name = 'Anonymous'

		token = get_token()
		if token:
			c.user_name = parse_token(token)[0]
			c.is_authorized = True