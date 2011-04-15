import re, urllib
from BeautifulSoup import BeautifulSoup

def reddit_login(username, password):
	""" This API seems to be unreliable.  Can't be relied on. """
	f = urllib.urlopen("http://www.reddit.com/api/login", 
			urllib.urlencode({'user': username, 'passwd': password}))
	return 'reddit_session=' in f.info().get('Set-Cookie', '')


def verify_token_in_thread(thread_url, reddit_username, token):
	f = urllib.urlopen(thread_url)
	soup = BeautifulSoup(f.read())
	f.close()

	html = []
	for i in soup.body.findAll(attrs = {'class': 'commentarea'}):
		for j in i.findAll(attrs = {'class': re.compile('author\s+gray|usertext-body')}, recursive = True):
			html.append(str(j).strip())

	# assemble a map containing all comments per user
	strip = re.compile('<.*?>|\n')
	user = None
	for chunk in html:
		if '<p>[deleted]</p>' in chunk: continue

		# look for a link, then the next one will be the content
		if chunk.startswith('<a href'):
			text = re.sub(strip, '', chunk)
			if text == reddit_username:
				user = text
		elif user and chunk.startswith('<div class="usertext-body">'):
			# it's our user - see if the token matches
			if re.sub(strip, '', chunk) == token:
				return True
			else:
				# didn't match, reset conditions
				user = None

	return False


