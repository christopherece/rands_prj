"""
Development settings for dskaranltd project.

- Run in Debug mode
- Use console backend for emails
- Enable Django Debug Toolbar
- Enable browsable API in dev
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-key-12345')

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'development@dskarans.com'

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'dskaranltd-dev-cache'
    }
}

# Debug settings
# ------------------------------------------------------------------------------
INTERNAL_IPS = ['127.0.0.1', 'localhost']

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local development environment settings
# ------------------------------------------------------------------------------
# Add any development-specific settings here

# Disable password validation for development
AUTH_PASSWORD_VALIDATORS = []

# Allow all hosts for development
ALLOWED_HOSTS = ['*']

# Disable HTTPS in development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Email settings for Gmail SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'dnskaransltd@gmail.com'
CONTACT_EMAIL = 'temiong1234@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dnskaransltd@gmail.com'
EMAIL_HOST_PASSWORD = 'ajlw nsfl ofjf fblg'

# Log all SQL queries
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}
