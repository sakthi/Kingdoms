from paste.httpexceptions import HTTPFound
from kingdoms.model import meta, Player
from pylons.controllers.util import abort
from pylons import request
import hashlib, logging

from sqlalchemy.orm.exc import NoResultFound

import logging, base64, datetime
log = logging.getLogger(__name__)

class MyPlugin(object):
	
	def authenticate(self, environ, identity):
		'''
			Try to find user in DB and check
			if supplied hashed password is the same as
			one we store
		'''
		try:
			username = identity['login']
			password = identity['password']
			log.debug('Authenticate: %s' % username)
		except KeyError:
			log.fatal('Login or Password is empty')
			return None
		
		try:
			known_user = meta.Session.query(Player).filter(Player.login == username).one()
			if hashlib.md5(password).hexdigest() != known_user.password_hash:
				log.fatal('Password mismatch')
				return None
			
			log.debug('user %s knows password well.' % known_user.login)
			return known_user.id
			
		except NoResultFound:
			log.fatal('AUTH: No such user')
			return None

	def add_metadata(self, environ, identity):
		'''
			Add metadata to user identity record
			Since we are the plugin who handles such
			operations
		'''
		id = identity.get('repoze.who.userid')
		timestamp = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
		token = '%s+%s' % (id, timestamp)
		log.debug('player id %s is granted with token %s' % (id, token))
		btoken = base64.b64encode(token)
		identity['kingdoms_auth_token'] = btoken
