"""
WSGI config for homebrewit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

print "In wsgi.py"
import django.core.handlers.wsgi 
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homebrewit.settings")
application = django.core.handlers.wsgi.WSGIHandler()

application = Cling(get_wsgi_application())

print "app start"
