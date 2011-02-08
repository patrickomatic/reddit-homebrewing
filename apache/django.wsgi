import os, sys
sys.path.append('/srv/homebrewit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'homebrewit.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
