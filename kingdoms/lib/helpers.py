"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from pylons import request, response, session, config, tmpl_context as c
import base64

def get_token():
	identity = request.environ.get('repoze.who.identity')
	if not identity:
		return None
	btoken = identity.get('kingdoms_auth_token')
	if not btoken:
		return None
	token = base64.b64decode(btoken)
	return token
	
def parse_token(token):
	index = token.find('+')
	id = token[:index]
	timestamp = token[index + 1:len(token)]
	if not 'T' in timestamp:
		timestamp = timestamp.replace(' ', 'T')
	return id, timestamp

def format_timestamp(timestamp):
	delta = datetime.datetime.now() - timestamp
	if delta.days > 0:
		if delta.days == 1:
			return '%s day ago on %s' % ( delta.days, timestamp.strftime("%A, %d. %B %Y %I:%M%p") )
		else:
			return '%s days ago on %s' % ( delta.days, timestamp.strftime("%A, %d. %B %Y %I:%M%p") )
	elif (delta.seconds	 < 3600):
		if (delta.seconds / 60) > 1:
			return '%s minutes ago' % (delta.seconds / 60)
		else:
			return '%s minute ago' % (delta.seconds / 60)
	else:
		return 'at %s ' % timestamp.strftime("%A, %d. %B %Y %I:%M%p")