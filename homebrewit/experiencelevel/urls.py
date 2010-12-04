from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.experiencelevel.views',
		(r'^level', 'change_level'),
)
