import urllib, urllib2, json, cookielib
from django.conf import settings


def retry(times, ex):
	""" A decorator which can be called as:

		@retry(5, Exception)
		def fn():
			raise Exception

	    and will call fn and if it throws an exception, it will keep
	    trying 5 times. """
	def retry_wrap(fn):
		def fn_wrap(*args, **kwargs):
			for i in range(times-1):
				try:
					return fn(*args, **kwargs)
				except ex:
					pass
			return fn(*args, **kwargs)
		return fn_wrap
	return retry_wrap


class RedditSession:
	def __init__(self, cookie_jar=None, modhash=None):
		self.cookie_jar = cookie_jar
		self.modhash = modhash


def reddit_api_url(url, data=None, session=None):
	if not session:
		session = RedditSession()
	elif data and not 'uh' in data and session.modhash:
		data['uh'] = session.modhash

	if data: 
		data = urllib.urlencode(data)

	if not session.cookie_jar:
		session.cookie_jar = cookielib.LWPCookieJar()

	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(session.cookie_jar))
	urllib2.install_opener(opener)

	return urllib2.urlopen(urllib2.Request('http://www.reddit.com/api' + url, data,
			{'User-Agent': settings.AUTHENTICATION_USER_AGENT}))


def reddit_login(username, password):
	""" Logs in a user and returns the modhash that can be used for the
	next request.  Returns None if login was unsuccessful.  """

	assert username and password
	
	session = RedditSession()

	fh = reddit_api_url("/login/" + username, 
		{'user': username, 'passwd': password, 'api_type': 'json'}, session)

	resp = json.loads(fh.read())

	if 'errors' in resp['json'] and len(resp['json']['errors']) == 0:
		session.modhash = resp['json']['data']['modhash']
		return session

	return None


def can_reddit_login(username, password):
	return reddit_login(username, password) is not None


def verify_token_in_thread(thread_url, reddit_username, token):
	""" Given a reddit thread, username and token it will scrape the thread
	and return True or False depending on if that user has posted the
	given token to that thread.  This has been abandoned for production use
	as it's got known issues with searching the thread once it has a "load 
	more comments" link. """

	reddit_username = unicode(reddit_username)

	f = urllib.urlopen(thread_url)
	thread = json.loads(f.read())
	f.close()

	for comment in thread[1]['data']['children']:
		if comment['data'].get('author') == reddit_username:
			if unicode(token) == comment['data']['body'].strip():
				return True

	return False


@retry(3, urllib2.HTTPError)
def set_flair(reddit_username, flair_class, reddit_session):
	reddit_api_url("/flair", {'r': 'homebrewing', 'name': reddit_username,
			'css_class': flair_class, 'text': ''}, reddit_session)
