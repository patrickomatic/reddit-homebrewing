import django.test
from homebrewit.related.models import *


class RelatedSubredditsTestCase(django.test.TestCase):
	def test_view_related(self):
		related_subreddit = RelatedSubreddit(display = 'Example Related Subreddit', url = 'http://reddit.com/r/toomanypuppies')
		related_subreddit.save()

		response = self.client.get('/related/')

		self.assertTemplateUsed(response, 'homebrewit_related_reddits.html')
		self.assertContains(response, 'Example Related Subreddit')
		self.assertContains(response, 'http://reddit.com/r/toomanypuppies')
		
