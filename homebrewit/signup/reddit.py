import re, urllib
from BeautifulSoup import BeautifulSoup

def reddit_login(username, password):
	""" This API seems to be unreliable.  Can't be relied on. """
	f = urllib.urlopen("http://www.reddit.com/api/login", 
			urllib.urlencode({'user': username, 'passwd': password}))
	return 'reddit_session=' in f.info().get('Set-Cookie', '')


def verify_token_in_thread(thread_url, reddit_username, token):
	f = urllib.urlopen(thread_url)
	html = BeautifulSoup(f.read())
	f.close()

	divz = []
	for i in html.body.findAll(attrs = {'class': 'commentarea'}):
		for j in i.findAll(attrs = {'class': re.compile('author\s+gray|usertext-body')}, recursive = True):
			divz.append(j)

	# assemble a map containing all comments per user
	comments, strip, count = {}, re.compile('<.*?>|\n'), 1
	for k in divz[::2]:
		user = re.sub(strip, '', str(k)).strip()
		text = re.sub(strip, '', str(divz[count])).strip()

		if not user in comments:
			comments[user] = [text]
		else:
			comments[user].append(text)

		count += 2

	# now see if any comments from that user match it
	if reddit_username in comments:
		for comment in comments[reddit_username]:
			if comment == token:
				return True
			
	return False


