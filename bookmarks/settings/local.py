from .base import *
from os.path import dirname, abspath
ROOT = dirname(abspath(__file__)).replace('\\', '/') + '/'

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT + 'db.sqlite3', 
    }
}
