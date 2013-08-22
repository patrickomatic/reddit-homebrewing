from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.profile.views',
    (r'^$', 'logged_in_profile'),
    (r'edit$', 'edit_profile'),
    (r'password$', 'change_password'),
    (r'^(?P<username>[\w_-]+)$', 'anonymous_profile'),
)
