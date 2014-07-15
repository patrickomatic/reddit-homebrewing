import os, sys, logging

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

    ROLLBAR = {
        'access_token': os.environ['ROLLBAR_ACCESS_TOKEN'],
        'environment': 'production',
        'branch': 'master',
        'root': PROJECT_PATH,
    }

    POSTMARK_API_KEY = os.environ['POSTMARK_API_KEY']
    POSTMARK_SENDER = 'do.not.reply@reddithomebrewing.com'
    POSTMARK_TEST_MODE = False
    POSTMARK_TRACK_OPENS = True
    EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
    os.path.join(PROJECT_PATH, 'templates/contest'),
    os.path.join(PROJECT_PATH, 'templates/experiencelevel'),
    os.path.join(PROJECT_PATH, 'templates/profile'),
    os.path.join(PROJECT_PATH, 'templates/related'),
    os.path.join(PROJECT_PATH, 'templates/signup'),
)

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = False

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
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
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
    'rest_framework',
    'south',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
) + OUR_APPS

def get_cache():
    import os
    try:
        os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHEDCLOUD_SERVERS'].replace(',', ';')
        os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHEDCLOUD_USERNAME']
        os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHEDCLOUD_PASSWORD']
        return { 
                'default': {
                    'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                    'TIMEOUT': 500,
                    'BINARY': True,
                    'OPTIONS': { 'tcp_nodelay': True }
                    }
                }
    except:
        return {
              'default': {
                  'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
                  }
              }

CACHES = get_cache()

LOGIN_URL = '/'
LOGOUT_URL = '/logout'

INTERNAL_IPS = ('127.0.0.1',)

AUTH_PROFILE_MODULE = 'signup.UserProfile'

WINNER_ICON = '/media/winner.png'

AUTHENTICATION_USER_AGENT = 'www.reddit.com/r/Homebrewing App (reddithomebrewing.com)'

MODERATOR_USERNAME, MODERATOR_PASSWORD = None, None
if 'HOMEBREWIT_MOD_CREDENTIALS' in os.environ:
    MODERATOR_USERNAME, MODERATOR_PASSWORD = os.environ['HOMEBREWIT_MOD_CREDENTIALS'].split(':')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(levelname)s] ' +
                       '%(pathname)s:%(lineno)s ' +
                       '%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
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
