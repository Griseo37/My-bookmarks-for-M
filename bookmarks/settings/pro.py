from .base import *

DEBUG = False

ADMINS = {
    ('Patryk N', 'niedzieckipatryk507@gmail.com'),
}

ALLOWE_HOSTS = ['www.stronadlaciebie.online', 'stronadlaciebie.online']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'sgpostgres',
        'PASSWORD': '976vxJV9^NR4wMNt',
    }
}
