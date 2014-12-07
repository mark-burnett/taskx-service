import dj_database_url
import os


TASKX_APP_NAME = os.environ['TASKX_APP_NAME']
TASKX_APP_MODULE = os.environ['TASKX_APP_MODULE']


BASE_DIR = os.path.abspath(os.environ['BASE_DIR'])


# Security settings
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
LOG_LEVEL = 'INFO'
if os.environ.get('DEBUG'):
    DEBUG = True
    TEMPLATE_DEBUG = True
    LOG_LEVEL = 'DEBUG'

ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_pgjson',

    TASKX_APP_MODULE,
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'taskx_service.urls'

WSGI_APPLICATION = 'taskx_service.wsgi.application'

APPEND_SLASH = False


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(),
}

AUTOCOMMIT = False
CONN_MAX_AGE = 600


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Logging configuration
LOGGING = {
    'version': 1,
    'loggers': {
        'django': {
            'level': LOG_LEVEL,
        },
    },
}


# DRF Configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGINATE_BY': 10,
}


# Celery Configuration
BROKER_URL = os.environ.get('RABBITMQ_BIGWIG_URL', 'amqp://')
CELERYD_PREFETCH_MULTIPLIER = 10
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ACKS_LATE = True
CELERY_TASK_SERIALIZER = 'json'
