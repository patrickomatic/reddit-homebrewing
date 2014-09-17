from django.conf.urls import patterns, url
from django.contrib import admin

from homebrewit.profile import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'edit$', views.edit_profile, name='edit_profile'),
    url(r'password$', views.change_password, name='change_password'),
    url(r'^(?P<username>[\w_-]+)|$', views.ProfileView.as_view(), name='profile'),
)
