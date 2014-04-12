from django.conf.urls import patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.experiencelevel.views',
		(r'^level$', 'change_level'),
		(r'^experience-styles.css$', 'experience_styles'),
)
