"""
Production settings for dskaranltd project.

- Use PostgreSQL database
- Enable security settings
- Configure logging
- Set up email
"""

from .base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'False'

# SECURITY SETTINGS
# ------------------------------------------------------------------------------
# Set this to your domain name in production
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'dskarans.com,www.dskarans.com').split(',')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Use PostgreSQL in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'dskaranltd'),
        'USER': os.environ.get('DB_USER', 'dskaranltd'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# CACHING
# ------------------------------------------------------------------------------
# Use Redis or Memcached in production
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dnskaransltd@gmail.com'
EMAIL_HOST_PASSWORD = 'ajlw nsfl ofjf fblg'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'dnskaransltd@gmail.com'
CONTACT_EMAIL = 'temiong1234@gmail.com'
SERVER_EMAIL = 'dnskaransltd@gmail.com'

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# STATIC FILES AND MEDIA
# ------------------------------------------------------------------------------
# Use a CDN or S3 for static and media files in production
# Example for AWS S3:
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_DEFAULT_ACL = 'public-read'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# For now, use local storage
STATIC_ROOT = '/var/www/dskaranltd/static'
MEDIA_ROOT = '/var/www/dskaranltd/media'

# CELERY CONFIGURATION (if using Celery for async tasks)
# ------------------------------------------------------------------------------
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE

# SECURITY HEADERS
# ------------------------------------------------------------------------------
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

# PERFORMANCE
# ------------------------------------------------------------------------------
# Enable GZip compression
MIDDLEWARE.insert(0, 'django.middleware.gzip.GZipMiddleware')  # noqa F405

# Enable template caching
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# COMPRESSION SETTINGS
# ------------------------------------------------------------------------------
# Enable GZip compression for faster page loads
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

# Add compressor to INSTALLED_APPS
INSTALLED_APPS += ['compressor']  # noqa F405

# CUSTOM SETTINGS
# ------------------------------------------------------------------------------
# Add any production-specific settings here

# Ensure the secret key is set in production
if 'SECRET_KEY' not in os.environ:
    raise RuntimeError("The SECRET_KEY setting must be set as an environment variable in production.")

# Ensure debug is off in production
if DEBUG:
    import warnings
    warnings.warn(
        'Debug mode is enabled in production. This is a security risk. "
        'Set DJANGO_DEBUG=False in your environment variables.",
        RuntimeWarning
    )
