from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.vercel.app',
    'omar-haji-portfolio.vercel.app',
    'omarhaji.com',
    'www.omarhaji.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'https://omar-haji-portfolio.vercel.app',
    'https://omarhaji.com',
    'https://www.omarhaji.com',
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
    'https://omarhaji.com',
    'https://www.omarhaji.com',
]