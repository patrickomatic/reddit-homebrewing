from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.contest.views',
		(r'^register/', 'register'),
)
