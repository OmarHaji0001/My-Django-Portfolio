from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.vercel.app',
    'omar-haji-portfolio.vercel.app',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'https://omar-haji-portfolio.vercel.app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': '6543',
    }
}

CORS_ALLOWED_ORIGINS = [
    'https://omar-haji-portfolio.vercel.app',
]