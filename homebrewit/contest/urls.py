from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.contest.views',
		(r'^register$', 'register'),
		(r'^/styles$', 'styles'),
		(r'^(?P<year>\d+)/winners$', 'winners'),
		(r'^(?P<year>\d+)/entries/(?P<entry_id>\d+)$', 'winners'),
)
