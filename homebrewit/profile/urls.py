from django.conf.urls import patterns, url
from django.contrib import admin

from.views import *

admin.autodiscover()

urlpatterns = patterns('homebrewit.profile.views',
    (r'edit$', 'edit_profile'),
    (r'password$', 'change_password'),
    url(r'^(?P<username>[\w_-]+)|$', ProfileView.as_view(), name='profile'),
)
