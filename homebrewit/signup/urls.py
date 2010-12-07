from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('homebrewit.signup.views',
    (r'^signup', 'signup'),
    (r'^login', 'login'),
    (r'^logout', 'logout'),
    (r'^$', 'index'),
)

