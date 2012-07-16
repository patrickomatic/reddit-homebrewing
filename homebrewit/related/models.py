from django.db import models

class RelatedSubreddit(models.Model):
	display = models.CharField(max_length = 100, verbose_name = 'Link Display')
	url = models.URLField(verbose_name = 'Subreddit URL')

	class Meta:
		ordering = ('display',)

	def __unicode__(self):
		return self.display
