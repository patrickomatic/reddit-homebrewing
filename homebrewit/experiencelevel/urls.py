from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.experiencelevel.views',
		(r'^level$', 'change_level'),
		(r'^experience-styles.css$', 'experience_styles'),
)
