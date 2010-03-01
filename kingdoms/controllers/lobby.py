import logging, os

from pylons import config, request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from kingdoms.model import meta, UnitTypeDescriptor
from kingdoms.lib.base import BaseController, render
from kingdoms.lib import GamesCache

log = logging.getLogger(__name__)

class LobbyController(BaseController):
	
	def overview(self):
		self.check_auth()
		c.units = meta.Session.query(UnitTypeDescriptor).all()
		c.games = GamesCache().list_games()
		return render('overview.mako')
		
	def skirmish(self):
		self.check_auth()
		c.units = meta.Session.query(UnitTypeDescriptor).all()
		return render('skirmish.mako')

	def unit_info(self, id):
		c.unit = meta.Session.query(UnitTypeDescriptor).filter(UnitTypeDescriptor.id == int(id)).one()
		return render('unit_info.mako')