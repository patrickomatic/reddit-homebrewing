import urllib, json


def reddit_login(username, password):
	""" This API seems to be unreliable.  Can't be relied on. """
	f = urllib.urlopen("http://www.reddit.com/api/login", 
			urllib.urlencode({'user': username, 'passwd': password}))
	return 'reddit_session=' in f.info().get('Set-Cookie', '')


def verify_token_in_thread(thread_url, reddit_username, token):
	reddit_username = unicode(reddit_username.lower())

	f = urllib.urlopen(thread_url)
	thread = json.loads(f.read())
	f.close()

	for comment in thread[1]['data']['children']:
		if 'author' in comment['data'] and comment['data']['author'].lower() == reddit_username:
			if unicode(token) == comment['data']['body'].strip():
				return True

	return False
