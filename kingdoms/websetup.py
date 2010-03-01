"""Setup the endless-insomnia application"""
import logging, os, hashlib, datetime

from sqlalchemy.orm.exc import NoResultFound

from kingdoms.config.environment import load_environment
from kingdoms.model import meta
from kingdoms.model import Player, UnitTypeDescriptor

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
	"""Place any commands to setup kingdoms here"""
	load_environment(conf.global_conf, conf.local_conf)
	# Create the tables if they don't already exist
	meta.metadata.create_all(bind=meta.engine)
	
	if len(meta.Session.query(UnitTypeDescriptor).all()) <= 0:
		footman = UnitTypeDescriptor()
		footman.short_name = u'Mercenary Footman'
		footman.long_name = u'Hired infantry with swords and shields.'
		footman.tile_type = u'footman'
		meta.Session.add(footman)
		
		archer = UnitTypeDescriptor()
		archer.short_name = u'Mercenary Archer'
		archer.long_name = u'Hired infantry with long bows.'
		archer.tile_type = u'archer'
		meta.Session.add(archer)
		
		meta.Session.commit()
		
	
	
	count = meta.Session.query(Player).count()
	if count == 0:
		user_name = os.getenv('USER')
		try:
			admin = meta.Session.query(Player).filter(Player.login == user_name).one()
		except NoResultFound:
			#login
			tmp = raw_input('What is your name, master (%s):' % user_name)
			if len(tmp) > 0:
				user_name = tmp
		
			#password
			password = raw_input('Enter your password:')
		
			#sex
			sex_txt = raw_input('Can I call you my daddy? (Keep empty for male by default)')
			if len(sex_txt) <= 0:
				sex = 1
			else:
				sex = 0
			owner = Player()
			owner.login = user_name
			owner.password_hash = hashlib.md5(password).hexdigest()
			owner.fullname = 'Great %s, master of realms. Ruler of mortals.' % user_name.capitalize()
			owner.timestamp = datetime.datetime.now()
			owner.email = user_name +'@kingdoms.com'
			owner.sex = sex
			meta.Session.add(owner)
			meta.Session.commit()
		finally:
			print 'What is your wish master, %s?' % user_name
	else:
		print '%d users are known' % count
		
	
