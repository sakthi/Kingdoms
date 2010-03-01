import logging, json, time

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from kingdoms.lib import KingdomsGame, GamesCache
from kingdoms.lib.base import BaseController, render, jsonify, object_encoder

from kingdoms.model import meta, Game
from sqlalchemy.orm.exc import NoResultFound
from kingdoms.lib import object_encoder
from kingdoms.lib import Unit
log = logging.getLogger(__name__)

class ApiController(BaseController):

	@jsonify
	def get_map(self):
		log.debug('AJAX API: get_map <- %s' % request.params)
		try:
			game_id = request.params.get('game_id')
			game = GamesCache().get_game(game_id)
			answer = {}
			answer['tileset'] = game.map.tileset
			answer['name'] = game.map.name
			answer['cells'] = game.map.cells
			answer['width'] = game.map.width
			answer['height'] = game.map.height
			answer['game_id'] = game.id
			log.debug('AJAX API: get_map -> %s' % json.dumps(answer, default=object_encoder))
			return answer
		except Exception, ex:
			log.error('AJAX API ERROR: %s %s' % (ex.__class__, str(ex)))
			return {'error' : str(ex)}
	
	@jsonify
	def get_object(self):
		log.debug('AJAX API: get_object <- %s' % request.params)
		try:
			game_id = request.params.get('game_id')
			game = GamesCache().get_game(game_id)
			answer = {}
			answer['obj'] = 'Nothing selected'
			answer['x'] = request.params.get('x')
			answer['y'] = request.params.get('y')
			mapx = ( int(request.params.get('x')) - int(request.params.get('left')) ) / 50
			mapy = ( int(request.params.get('y')) - int(request.params.get('top')) )  / 50
			answer['mapx'] = mapx
			answer['mapy'] = mapy
			answer['game_id'] = game.id
			obj = game.map.cells[mapx][mapy]
			if obj:
				answer['obj'] = obj
				if isinstance(obj, Unit):
					unit_type = {}
					unit_type['short_name'] = obj.unit_type.short_name
					unit_type['long_name'] = obj.unit_type.long_name
					answer['unit_type'] = unit_type
			log.debug('AJAX API: get_object -> %s' % json.dumps(answer, default=object_encoder))
			return answer
			
		except Exception, ex:
			log.error('AJAX API ERROR: %s %s' % (ex.__class__, str(ex)))
			return {'error' : str(ex)}