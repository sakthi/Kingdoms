import logging

from pylons import config, request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from routes import redirect_to, url_for
from kingdoms.lib.base import BaseController, render
from kingdoms.lib import KingdomsGame, GamesCache

log = logging.getLogger(__name__)

class EngineController(BaseController):
	def generate(self):
		players = []
		for i in xrange(0, 4):
			faction = request.params.get('player_%s_faction' % i)
			if faction != 'off':
				footman = request.params.get('player_%s_footman' % i)
				archer = request.params.get('player_%s_archer' % i)
				player_info = (faction, int(footman), int(archer))
				players.append( player_info )
				log.debug('player info:')
				log.debug(player_info)
				
		log.debug('generating map for %d players' % len(players))
			
		game = KingdomsGame(config, players)
		GamesCache().add_game(game)
		log.debug('created game %s' % game.id)
		return redirect_to(url_for(action='map', id = game.id))
		
	def map(self, id):
		try:
			c.game = GamesCache().get_game(id)
		except AttributeError:
			return "Your game game is outdated, most propably your game is over. Check <a href=\"/lobby/overview\">the overiview</a>"
		return render('map.mako')
