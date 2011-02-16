from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	email = models.EmailField()
	address_1 = models.CharField(max_length=255)
	address_2 = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	zip_code = models.PositiveIntegerField()

	def get_profile(self):
		try:
			return self.get_profile()
		except UserProfile.DoesNotExist:
			return None

        def __unicode__(self):
            return self.user.username
