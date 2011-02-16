import urllib

def reddit_login(username, password):
	f = urllib.urlopen("http://www.reddit.com/api/login", 
			urllib.urlencode({'user': username, 'passwd': password}))
	return 'reddit_session=' in f.info().get('Set-Cookie', '')
