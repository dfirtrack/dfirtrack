"""
Django settings for DFIRTrack project.
"""

from dfirtrack.config import LOGGING_PATH
import logging
import os
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.CRITICAL)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGEME'

# Application definition

INSTALLED_APPS = [
    'dfirtrack_main',
    'dfirtrack_artifacts',
    'dfirtrack_api',
    'dfirtrack_config',
    'rest_framework',
    'django_q',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dfirtrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dfirtrack.wsgi.application'


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/system/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_formatter': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'customlog': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOGGING_PATH + '/' + 'dfirtrack.log',
	    'formatter': 'std_formatter',
        },
    },
    'loggers': {
        'dfirtrack_artifacts': {
            'handlers': ['customlog'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'dfirtrack_main': {
            'handlers': ['customlog'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

Q_CLUSTER = {
    'name': 'dfirtrack',
    'workers': 4,
    'orm': 'default',
    'label': 'Django Q',
    'sync': True,
}

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES' : [
   'rest_framework.authentication.BasicAuthentication',
   'rest_framework.authentication.SessionAuthentication',
],
'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated',
   ],
}

# import local settings for development
try:
    from .local_settings import ALLOWED_HOSTS, DATABASES, DEBUG, STATIC_ROOT

except ImportError:     # coverage: ignore branch
    ''' default values for testing purposes '''

    # change to True for debugging
    DEBUG = False

    # add IP or FQDN if relevant
    ALLOWED_HOSTS = ['localhost']

    # Database - check environment variables for context
    if "CI" in os.environ:
        # use PostgreSQL for GitHub action
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'github_actions',
                'USER': 'dfirtrack',
                'PASSWORD': 'dfirtrack',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        }
    else:
        # use SQLite3 otherwise (for local setup without dfirtrack.local_settings)
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'dfirtrack.sqlite3'),
            }
        }

    STATIC_ROOT = '/var/www/html/static/'
