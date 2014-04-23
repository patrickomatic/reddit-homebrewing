import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Django settings for homebrewit project.
PROD_DB_URL = 'DATABASE_URL'

DEBUG = not PROD_DB_URL in os.environ
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
            }
    }
else:
    import dj_database_url
    DATABASES = { 'default': dj_database_url.config(default=os.environ[PROD_DB_URL]) }


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = 'homebrewit.wsgi.application'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '%jz%s8d*sa--zso2572_s#6z8+z79gfyrypfc&rkp-04t3&@tg')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'homebrewit.urls'

OUR_APPS = (
        'homebrewit.contest',
        'homebrewit.experiencelevel',
        'homebrewit.signup',
        'homebrewit.profile',
        'homebrewit.related',
)

INSTALLED_APPS = (
        'south',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
        'django.contrib.staticfiles',
) + OUR_APPS

# If someone wants to work on this locally, they shouldn't have
# to deal with stupid memcached issues...
if DEBUG:
	CACHE_BACKEND = 'dummy:///'
else:
	CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

LOGIN_URL = '/'
LOGOUT_URL = '/logout'

INTERNAL_IPS = ('127.0.0.1',)

AUTH_PROFILE_MODULE = 'signup.UserProfile'


# mail config
DEFAULT_FROM_EMAIL = 'do.not.reply@reddithomebrewing.com'
EMAIL_HOST = 'cmx.dyercpa.com'

WINNER_ICON = '/media/winner.png'

AUTHENTICATION_USER_AGENT = 'www.reddit.com/r/Homebrewing App (reddithomebrewing.com)'

MODERATOR_USERNAME, MODERATOR_PASSWORD = None, None
if 'HOMEBREWIT_MOD_CREDENTIALS' in os.environ:
	MODERATOR_USERNAME, MODERATOR_PASSWORD = os.environ['HOMEBREWIT_MOD_CREDENTIALS'].split(':')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
