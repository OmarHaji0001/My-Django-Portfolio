from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': '6543',
        'TEST': {
            'NAME': 'test_portfolio_local',
        },
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]