# -*- coding: utf-8 -*- 
from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'orientation_db',
        'USER': 'hesham',
        'PASSWORD': 'shammy',
        'HOST': '',
        'PORT': '',
    }
}