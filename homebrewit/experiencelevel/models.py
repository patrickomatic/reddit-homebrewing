from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class ExperienceLevel(models.Model):
	name = models.CharField(max_length=255)
	img_url = models.FilePathField(path=settings.MEDIA_ROOT)

	def __unicode__(self):
		return self.name


class UserExperienceLevel(models.Model):
	user = models.ForeignKey(User, unique=True)
	experience_level = models.ForeignKey(ExperienceLevel)

	def __unicode__(self):
		return "%s: %s" % (self.user, self.experience_level)

	def to_css(self):
		# XXX print the CSS needed to show the experience level
		return ""
