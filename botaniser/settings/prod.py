from botaniser.settings.common import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_APP_SECRET = os.environ['FACEBOOK_APP_SECRET']

INSTALLED_APPS = INSTALLED_APPS + ('storages',)

AWS_STORAGE_BUCKET_NAME = "botaniser-media"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL


DATABASES = {
    'default':
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER' : os.environ['DB_USER'],
        'PASSWORD' : os.environ['DB_PWD'],
        'HOST' : os.environ['DB_HOST'],
        'PORT' : '5432',
    }
}

