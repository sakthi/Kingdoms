import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from kingdoms.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AuthController(BaseController):

	def login(self):
		return render('login.mako')

	def auth(self):
		identity = session.get('repoze.who.identity')
		if not identity is None:
			if session.get('came_from'):
				log.debug('redirecting to %s' % session['came_from'])
				return redirect_to(session['came_from'])
			else:
				log.debug('redirecting to /lobby/overiview [default]')
				return redirect_to(url_for(controller = 'lobby', action = 'overiview'))
		else:
			log.error('no identity found')



	def logout(self):
		identity = session.get('repoze.who.identity')
		if not identity:
			log.info('no identity, redirecting to login page.')
		else:
			log.error('identity %s in LOGOUT!' % identity)

		return redirect_to(url_for(action = 'login'))