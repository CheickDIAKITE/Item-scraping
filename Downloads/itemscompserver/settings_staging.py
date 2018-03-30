from .common import *

from urllib.parse import urlparse

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfjg5ghtgs2opl',
        'USER': 'bboihetiofmlkh',
        'PASSWORD': '30b77b3b43d88ac0d4659cd0bedf52156da42bc2d076e53d2f54a5b684028e4e',
        'HOST': 'ec2-23-21-194-171.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

AWS_ACCESS_KEY_ID = 'AKIAIDOKUUZO7UYBUWWQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'pruebarobin'
AWS_S3_REGION_NAME = 'us-west-2'

CORS_ORIGIN_ALLOW_ALL = True

# Django Cors Headers
# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000'
#     'itemscompareform.herokuapp.com',
#     'null'
# )

# CORS_ALLOW_METHODS = default_methods + (
#     'JSONP',
# )

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'content-type',
    'origin',
    'user-agent',
    'x-requested-with',
    'access-control-allow-headers',
    'access-control-allow-methods',
    'access-control-allow-origin',
)
