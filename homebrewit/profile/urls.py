from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.profile.views',
    (r'^', 'profile'),
    (r'^(?P<username>\w+)', 'profile'),
)
