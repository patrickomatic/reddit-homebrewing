from django.conf import settings
from django.db import models
from os.path import join
from django.contrib.auth.models import User


class ExperienceLevel(models.Model):
	name = models.CharField(max_length=255)
#	description = models.CharField(max_length=500)
	img_url = models.FilePathField(path=join(settings.MEDIA_ROOT, 'images/icons/experience_levels'))
	css_img_url = models.FilePathField(path=join(settings.MEDIA_ROOT, 'images/icons/experience_levels'))
	order = models.PositiveSmallIntegerField()

	class Meta:
		ordering = ('order',)


	def get_absolute_url(self):
		return 'http://reddithomebrewing.com' + self.img_url.replace(settings.MEDIA_ROOT, '/media')

	def get_absolute_css_url(self):
		return 'http://reddithomebrewing.com' + self.css_img_url.replace(settings.MEDIA_ROOT, '/media')

	def get_reddit_css_icon(self):
		return self.name.lower()

	def __unicode__(self):
		return self.name


class UserExperienceLevel(models.Model):
	user = models.ForeignKey(User, unique=True)
	experience_level = models.ForeignKey(ExperienceLevel)

	def __unicode__(self):
		return "%s: %s" % (self.user, self.experience_level)
