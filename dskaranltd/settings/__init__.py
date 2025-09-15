"""
Default settings for dskaranltd project.

In production, use production.py settings.
For development, use development.py settings.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Import the appropriate settings based on the environment
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .production import *  # noqa
else:
    from .development import *  # noqa

if 'SECRET_KEY' not in locals() and 'SECRET_KEY' not in os.environ:
    raise RuntimeError("SECRET_KEY must be set in the environment or settings file.")

# Ensure the database is configured
if 'DATABASES' not in locals():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Ensure static and media roots are set
if 'STATIC_ROOT' not in locals():
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if 'MEDIA_ROOT' not in locals():
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'STATIC_URL' not in locals():
    STATIC_URL = '/static/'

# Core app is already included in base.py
