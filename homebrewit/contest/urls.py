from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework import routers
from homebrewit.contest import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'beer_styles', views.BeerStyleListView)

urlpatterns = patterns('homebrewit.contest.views',
        (r'^(?P<year>\d+)/$', 'contest_year'),
        (r'^(?P<year>\d+)/register$', 'register'),
        (r'^(?P<year>\d+)/styles/(?P<style_id>\d+)/entries/(?P<entry_id>\d+)$', 'entry'),
        url(r'^(?P<year>\d+)/styles/(?P<style_id>\d+)/entries$', views.EntriesListView.as_view(), name="contest_entries"),
        (r'^(?P<year>\d+)/styles/(?P<style_id>\d+)$', 'style'),
        url(r'^(?P<year>\d+)/beer_styles', views.BeerStyleListView.as_view()),
        (r'^judgeentry$', 'entry_judging_form'),
)
