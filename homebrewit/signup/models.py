from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address_1 = models.CharField(max_length=255, null=True, blank=True)
	address_2 = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	zip_code = models.PositiveIntegerField(null=True, blank=True)

	def get_profile(self):
		try:
			return self.get_profile()
		except UserProfile.DoesNotExist:
			return None

