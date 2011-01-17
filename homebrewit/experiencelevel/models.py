from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class ExperienceLevel(models.Model):
	name = models.CharField(max_length=255)
	img_url = models.FilePathField(path=settings.MEDIA_ROOT)

	def get_absolute_url(self):
		return self.img_url.replace(settings.MEDIA_ROOT, '/media')

	def __unicode__(self):
		return self.name


class UserExperienceLevel(models.Model):
	user = models.ForeignKey(User, unique=True)
	experience_level = models.ForeignKey(ExperienceLevel)


	def to_css(self):
		return """
a[href*="user/%(username)s"]:after {
	content: url(%(icon_url)s);
}
		""" % {
				'username': self.user.username, 
				'icon_url': self.experience_level.get_absolute_url(),
				}

	def __unicode__(self):
		return "%s: %s" % (self.user, self.experience_level)
