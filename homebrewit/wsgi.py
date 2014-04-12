"""
WSGI config for homebrewit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import django.core.handlers.wsgi 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homebrewit.settings")
application = django.core.handles.wsgi.WSGIHandler()
