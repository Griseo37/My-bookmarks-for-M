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
        'PASSWORD': '976vxJV9%5ENR4wMNt',
        'HOST': 'SG-Bookmarks-2277-pgsql-master.servers.mongodirector.com',
        'PORT': '5432',
    }
}
