from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address_1 = models.CharField(max_length=255, null=True, blank=True)
	address_2 = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	state = models.CharField(max_length=255, null=True, blank=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	zip_code = models.CharField(max_length=255, null=True, blank=True)

	def __unicode__(self):
		return self.user.username

	def is_complete(self):
		# check some fields that shouldn't be null
		return None in (self.user, self.user.email, self.country)


def create_user_profile(sender, instance, created, **kwargs):
	""" Signal handler which creates the profile if it doesn't exist. """
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

# register the handler
post_save.connect(create_user_profile, sender=User)
