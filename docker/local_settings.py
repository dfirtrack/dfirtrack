"""
Django settings for DFIRTrack project provided with Ansible.

These settings extend the defaul dfirtrack.settings.
"""

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.getenv('FQDN', '{{ fqdn }}'), 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'dfirtrack'),
        'USER': os.getenv('DB_USER', '{{ postgresql_user }}'),
        'PASSWORD': os.getenv('DB_PASSWORD', '{{ postgresql_user_password }}'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', 5432),
    }
}

STATIC_ROOT = '/var/www/html/static/'