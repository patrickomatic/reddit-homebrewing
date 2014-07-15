from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.TextField(null=True, blank=True)
    address_1 = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zip_code = models.TextField()
    country = models.TextField()

    class Meta:
        ordering = ('user__username',)

    def __unicode__(self):
        return self.user.username
