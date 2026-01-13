"""
Django settings for DFIRTrack project provided with Ansible.

These settings extend the default dfirtrack.settings.
"""

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = [os.getenv('FQDN'), 'localhost']
CSRF_TRUSTED_ORIGINS = ['https://'+os.getenv('FQDN', 'localhost'), 'http://'+os.getenv('FQDN', 'localhost')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'dfirtrack'),
        'USER': os.getenv('DB_USER', 'dfirtrack'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'dfirtrack'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', 5432),
    }
}

STATIC_ROOT = '/var/www/html/static/'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# OIDC authentication settings
OIDC_ENABLED = os.getenv('OIDC_ENABLED', 'False') == 'True'
OIDC_RP_CLIENT_ID = os.getenv('OIDC_RP_CLIENT_ID', '')
OIDC_RP_CLIENT_SECRET = os.getenv('OIDC_RP_CLIENT_SECRET', '')
OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv('OIDC_OP_AUTHORIZATION_ENDPOINT', '')
OIDC_OP_TOKEN_ENDPOINT = os.getenv('OIDC_OP_TOKEN_ENDPOINT', '')
OIDC_OP_USER_ENDPOINT = os.getenv('OIDC_OP_USER_ENDPOINT', '')
OIDC_OP_JWKS_ENDPOINT = os.getenv('OIDC_OP_JWKS_ENDPOINT', '')
OIDC_RP_SIGN_ALGO = os.getenv('OIDC_RP_SIGN_ALGO', 'RS256')
SITE_URL = os.getenv('SITE_URL', '')
OIDC_CREATE_USER = False
