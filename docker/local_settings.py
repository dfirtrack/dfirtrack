"""
Django settings for DFIRTrack project provided with Ansible.

These settings extend the defaul dfirtrack.settings.
"""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['{{ fqdn }}','localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfirtrack',
        'USER': '{{ postgresql_user }}',
        'PASSWORD': '{{ postgresql_user_password }}',
        'HOST': 'db',
        'PORT': '',
    }
}

STATIC_ROOT = '/var/www/html/static/'