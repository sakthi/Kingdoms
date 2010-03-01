# Kingdoms Game
# AwesomeStanlyLabs 2010

import json
import uuid
import logging
import random
from kingdoms.model import meta, UnitTypeDescriptor, HiredUnit
from paste.registry import StackedObjectProxy

log = logging.getLogger(__name__)

games_cache = StackedObjectProxy()

class MapException(Exception):
	pass

class MapObject(object):	
	def __init__(self, type, rotation = 'left'):
		self.type = type
		self.rotation = rotation

	def __call__(self):
		return '%s/%s.png' % (self.type, self.rotation)
		
def object_encoder(obj):
	if isinstance(obj, MapObject):
		props = {}
		for prop in dir(obj):
			if prop.startswith('_'):
				continue
			props[prop] = getattr(obj, prop)
		return props

class Moveable(MapObject):
	def move(self):
		pass
		
class Unit(Moveable):
	def __init__(self, faction, count, unit_type_id, rotation = 'left', unit_id = None):
		self.faction = faction
		self.unit_type_id = unit_type_id
		if unit_id:
			self.unit_id = unit_id
			self.unit_info = meta.Session.query(HiredUnit).filter(HiredUnit.id == unit_id).one()
			#copy from saved data
			self.banner = self.unit_info.banner
			self.count = self.unit_info.count
			self.unit_type = self.unit_info.unit_type
		else:
			self.unit_id = -1 * random.randint(1, 10000)
			self.unit_type = meta.Session.query(UnitTypeDescriptor).filter(UnitTypeDescriptor.id == unit_type_id).one()
			self.banner = 'banner-%s.png' % faction
			self.count = count
		
		super(Unit, self).__init__(self.unit_type.tile_type, rotation)
		
class KingdomsMap(object):
	width = 0
	height = 0
	cells = {}
	tileset = 'default'
	name = 'Generated Map'
	
	@classmethod
	def generate(cls, width, height, players):
		inst = cls();
		inst.width = width
		inst.height = height
		for x in xrange(0, width):
			inst.cells[x] = {}
			for y in xrange(0, height):
				inst.cells[x][y] = None
		
		for i in xrange(0, len(players)):
			log.debug('adding player %s' % players[i][0])
			inst.cells[3 + i][4] = Unit(players[i][0], int(players[i][1]), 1)
			inst.cells[3 + i][5] = Unit(players[i][0], int(players[i][2]), 2)
		return inst
		
class GamesCache(object):
	"""
	This is the BORG design pattern. It makes 
	all instances of this class share the same state
	by reinitializing its __dict__ with shared class member
	"""
	__shared_state = {}

	def __init__(self):
		self.__dict__ = self.__shared_state
		
	def get_game(self, id):
		log.debug('reading game %s' % id)
		return self._games[id]
		
	def add_game(self, game):
		if not hasattr(self, '_games'):
			log.debug('initializing games cache')
			self._games = {}
		log.debug('adding game %s' % game.id)
		self._games[game.id] = game
		
	def list_games(self):
		if hasattr(self, '_games'):
			return self._games.keys()
		else:
			return []


class KingdomsGame(object):
	def __init__(self, config, players):
		self.id = str(uuid.uuid4())
		self.config = config
		self.map = KingdomsMap.generate(10, 10, players)