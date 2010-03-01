"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.types import *
from sqlalchemy.orm import mapper
from kingdoms.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine

players_table = sa.Table('player', meta.metadata,
	sa.Column('id', Integer, primary_key = True),
	sa.Column('login', String(20), unique = True, nullable = False),
	sa.Column('email', String(255), unique = True, nullable = False),
	sa.Column('fullname', Unicode(255), nullable = False),
	sa.Column('password_hash', String(32), nullable = False),
	sa.Column('sex', Integer, nullable = True),
	sa.Column('timestamp', TIMESTAMP, nullable = False)
)

class HiredUnit(meta.Base):
	__tablename__ = 'unit';

	id = sa.Column(Integer, primary_key = True)
	count = sa.Column(Integer, nullable = False)
	banner = sa.Column(Unicode, nullable = False)
	type_id = sa.Column(Integer, sa.ForeignKey('unit_type.id'), nullable = False)
	army_id = sa.Column(Integer, sa.ForeignKey('army.id'), nullable = False)

class UnitTypeDescriptor(meta.Base):
	__tablename__ = 'unit_type'

	id = sa.Column(Integer, primary_key = True)
	short_name = sa.Column(Unicode(150), nullable = False)
	long_name = sa.Column(Unicode(1000), nullable = False)

	tile_type = sa.Column(Unicode(50), nullable = False)
	
	units_of_type = orm.relation(HiredUnit,  \
		backref=orm.backref('unit_type', remote_side='HiredUnit.type_id'))

class Hero(meta.Base):
	__tablename__ = 'hero'
	id = sa.Column(Integer, primary_key = True)
	player_id = sa.Column(Integer, sa.ForeignKey('player.id'), nullable = False)

class Army(meta.Base):
	__tablename__ = 'army'

	id = sa.Column(Integer, primary_key = True)
	hero_id = sa.Column(Integer, sa.ForeignKey('hero.id'), nullable = False)
	player_id = sa.Column(Integer, sa.ForeignKey('player.id'), nullable = False)
	
	units = orm.relation(HiredUnit,  \
		backref=orm.backref('in_army', remote_side='HiredUnit.army_id'))

class Game(meta.Base):
	__tablename__ = 'game';

	id = sa.Column(Integer, primary_key = True)
	player_0 = sa.Column(Integer, sa.ForeignKey('player.id'), nullable = False)
	player_1 = sa.Column(Integer, sa.ForeignKey('player.id'))
	player_2 = sa.Column(Integer, sa.ForeignKey('player.id'))
	player_3 = sa.Column(Integer, sa.ForeignKey('player.id'))

class GameMapCell(meta.Base):
	__tablename__ = 'game_cell';
	id = sa.Column(Integer, primary_key = True)
	x = sa.Column(Integer, nullable = False)
	y = sa.Column(Integer, nullable = False)
	unit_id = sa.Column(Integer, sa.ForeignKey('unit.id'))
	game_id = sa.Column(Integer, sa.ForeignKey('game.id'))
	
	unit = orm.relation(HiredUnit,  \
		backref=orm.backref('on_map_cell', remote_side='HiredUnit.id'))	
	
	game = orm.relation(Game,  \
		backref=orm.backref('cells', remote_side='Game.id'))

class Player(object):
	#__tablename__ = 'player'

	armies = orm.relation(Army, cascade='all', \
		backref=orm.backref('owner', remote_side='Army.player_id'))

	heroes = orm.relation('owner', cascade='all', \
		backref=orm.backref('owner', remote_side='Hero.player_id'))

	def __str__(self):
		return '%s (%s)' % (self.login, self.fullname)
		
mapper(Player, players_table)