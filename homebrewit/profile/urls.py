from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.profile.views',
    (r'^$', 'logged_in_profile'),
    (r'edit$', 'edit_profile'),
    (r'^(?P<username>\w+)$', 'anonymous_profile'),
)
