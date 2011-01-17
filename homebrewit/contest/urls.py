from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.contest.views',
		(r'^register$', 								'register'),
		(r'^(?P<year>\d+)/styles$', 					'styles'),
		(r'^(?P<year>\d+)/styles/(?P<style_id>\d+)$', 	'style'),
		(r'^(?P<year>\d+)/entries/(?P<entry_id>\d+)$', 	'entry'),
		(r'^(?P<year>\d+)/$', 							'contest_year'),
)
