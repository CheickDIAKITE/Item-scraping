import os
from os.path import join, normpath
import sys
from urllib.parse import urlparse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TMP_DIR = join(BASE_DIR, 'tmp')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vst=o6#osg=8xi!gzxtp62p2cxj^g9-l)2&!ggcy8xi&sjtsk*'

# Add apps/ to the Python path
# ============================
sys.path.append(normpath(join(BASE_DIR, 'apps')))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_rq",
    'api',
    # django-cors-headers
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'itemscompserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'itemscompserver.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

redis_url = urlparse(os.environ.get('REDIS_URL'))
CACHES = {
    "default": {
         "BACKEND": "redis_cache.RedisCache",
         "LOCATION": "{0}:{1}".format(redis_url.hostname, redis_url.port),
         "OPTIONS": {
             "PASSWORD": redis_url.password,
             "DB": 0,
         }
    }
}

RQ_QUEUES = {
    'default': {
        'URL': 'redis://h:p28962765c915b2ea1c5a40878f3529c86ba1163bf3933c5b68fa6d609e779241@ec2-34-206-75-227.compute-1.amazonaws.com:21109/0',
        'DEFAULT_TIMEOUT': 3600,
    },
    'high': {
        'URL': 'redis://h:p28962765c915b2ea1c5a40878f3529c86ba1163bf3933c5b68fa6d609e779241@ec2-34-206-75-227.compute-1.amazonaws.com:21109/0',
        'DEFAULT_TIMEOUT': 3600,
    },
    'low': {
        'URL': 'redis://h:p28962765c915b2ea1c5a40878f3529c86ba1163bf3933c5b68fa6d609e779241@ec2-34-206-75-227.compute-1.amazonaws.com:21109/0',
        'DEFAULT_TIMEOUT': 3600,
    }
}

# Test runner with no database creation
TEST_RUNNER = 'apps.api.tests.NoDbTestRunner'
