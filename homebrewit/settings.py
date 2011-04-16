import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))

# Django settings for homebrewit project.

DEBUG = not 'HOMEBREWIT_DB_PASS' in os.environ
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Patrick Carroll', 'patrick@patrickomatic.com'),
     ('Charles Hamilton', 'musashi@nefaria.com'),
)

MANAGERS = ADMINS

if DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', 
			'NAME': os.path.expanduser(os.path.join('~', '.homebrewit-db')),
			'USER': '',                     
			'PASSWORD': '',                
			'HOST': '',                   
			'PORT': '',                  
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2', 
			'NAME': 'homebrewit',                      
			'USER': 'homebrewit',                     
			'PASSWORD': os.environ['HOMEBREWIT_DB_PASS'],
			'HOST': '',
			'PORT': '', 
		}
	}

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') 
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '%jz%s8d*sa--zso2572_s#6z8+z79gfyrypfc&rkp-04t3&@tg'

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

if DEBUG:
	OUR_APPS = (
	    'contest',
	    'experiencelevel',
	    'signup',
	    'profile',
	)
else:
	OUR_APPS = (
	    'homebrewit.contest',
	    'homebrewit.experiencelevel',
	    'homebrewit.signup',
	    'homebrewit.profile',
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

# If someone wants to work on this locally, they shouldn't have
# to deal with stupid memcached issues...
if DEBUG:
	CACHE_BACKEND = 'dummy:///'
else:
	CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# for some reason, when allowing django to run all tests, some of them
# fail with a NoReverseMatch exception
TEST_RUNNER = 'local_tests.run_tests'

LOGIN_URL = '/'
LOGOUT_URL = '/logout'

INTERNAL_IPS = ('127.0.0.1',)

AUTH_PROFILE_MODULE = 'signup.UserProfile'

WINNER_ICON = '/media/winner.png'

DEFAULT_FROM_EMAIL = 'root@cmx.dyercpa.com'

REDDIT_REGISTRATION_THREAD = 'http://www.reddit.com/r/Homebrewing/comments/gqrp5/post_your_tokens_here_for_reddithomebrewingcom/'
