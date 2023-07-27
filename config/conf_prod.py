import os

from .settings import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "generate_")

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': 'django',
        'PASSWORD': 'ecogumus',
        'HOST': "127.0.0.1",
        'PORT': '5432',
    }
}

del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / 'static'