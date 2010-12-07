from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.contest.views',
		(r'^winner-styles.css$', 'winner_styles'),
		(r'^register$', 'register'),
		(r'^styles$', 'styles'),
		(r'^(?P<year>\d+)/$', 'contest_year'),
		(r'^(?P<year>\d+)/entries/(?P<entry_id>\d+)$', 'entry'),
)
