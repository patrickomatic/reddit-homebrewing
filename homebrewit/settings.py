import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))

# Django settings for homebrewit project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Patrick', 'patrick@patrickomatic.com'),
)

MANAGERS = ADMINS

if DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': '/tmp/homebrewit',                      # Or path to database file if using sqlite3.
			'USER': '',                      # Not used with sqlite3.
			'PASSWORD': '',                  # Not used with sqlite3.
			'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'homebrewit',                      # Or path to database file if using sqlite3.
			'USER': 'homebrewit',                      # Not used with sqlite3.
			'PASSWORD': '',                  # Not used with sqlite3.
			'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') 
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%jz%s8d*sa--zso2572_s#6z8+z79gfyrypfc&rkp-04t3&@tg'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#	'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'homebrewit.urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_PATH, 'templates')
)

OUR_APPS = (
    'contest',
    'experiencelevel',
    'signup',
    'profile',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
#	'debug_toolbar',
) + OUR_APPS

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# for some reason, when allowing django to run all tests, some of them
# fail with a NoReverseMatch exception
TEST_RUNNER = 'local_tests.run_tests'

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

INTERNAL_IPS = ('127.0.0.1',)

AUTH_PROFILE_MODULE = 'signup.UserProfile'

WINNER_ICON = '/media/winner.png'
