from django.conf import settings
import urllib, urllib2, json


def reddit_login(username, password):
	if not username or not password: return False

	req = urllib2.Request("http://www.reddit.com/api/login", 
			urllib.urlencode({'user': username, 'passwd': password}),
			{'User-Agent': settings.AUTHENTICATION_USER_AGENT})
	resp = urllib2.urlopen(req)

	return 'reddit_session=' in resp.info().get('Set-Cookie', '')


def verify_token_in_thread(thread_url, reddit_username, token):
	reddit_username = unicode(reddit_username)

	f = urllib.urlopen(thread_url)
	thread = json.loads(f.read())
	f.close()

	for comment in thread[1]['data']['children']:
		if 'author' in comment['data'] and comment['data']['author'] == reddit_username:
			if unicode(token) == comment['data']['body'].strip():
				return True

	return False
