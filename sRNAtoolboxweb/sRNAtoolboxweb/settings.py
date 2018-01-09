"""
Django settings for untitled project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.files.storage import FileSystemStorage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^qn#c))1g9tb103+q4@04gk^**9#@6=kp(i4lz%$ron%yumut='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'crispy_forms',
    'sRNAfuncTerms',
    'progress',
    'helpers',
    'sRNABench',
    'sRNAblast',
    'miRNAconstarget',
    'sRNAjBrowser',
    'sRNAgFree',
    'django_tables2',
    'dajax',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sRNAtoolboxweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'sRNAtoolboxweb.wsgi.application'

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'X-Prototype-Version',
    'x-csrftoken'
)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

FS = FileSystemStorage("/shared/sRNAtoolbox/webData")
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

MEDIA_ROOT = os.path.join(BASE_DIR, "upload")

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sRNAtoolboxweb', 'static'),
    MEDIA_ROOT

]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

CONF = {
    "sRNAtoolboxSOBasePath": "/shared/sRNAtoolbox",
    "sRNAtoolboxSODataPath": "/shared/sRNAtoolbox/webData",
    "jBrowserSOPathGenome": "/var/www/sRNAtoolbox/sRNAjBrowser/genomes",
    "jBrowserSOPathTmpUsers": "/var/www/sRNAtoolbox/sRNAjBrowser/tmpUsers",
    "jBrowserWWWPath": "/sRNAtoolbox/sRNAjBrowser",
    "jBrowserWWWPathTmpUsers": "/sRNAtoolbox/sRNAjBrowser/tmpUsers",
    "jBrowserWWWPathGenome": "/sRNAtoolbox/sRNAjBrowser/genomes",
    "seqObj": "/srv/shared/sRNAtoolboxDB/seqOBJ",
    "annotationPath": "/shared/sRNAtoolboxDB/jBrowserAnnot",
    "species": "sRNAtoolboxDB/species.txt",
    "speciesAnnotation": "/home/aruedamartin/annotation.txt",
    "targetAnnotation": "/shared/sRNAtoolboxDB/targetAnnot.txt",
    "db": "/shared/sRNAtoolboxDB",
    "exec": "/shared/sRNAtoolboxDB/exec",
    "RNAcentral": "/shared/sRNAtoolboxDB/dbs/rnacentral_active.fasta",
    "tRNA": "/shared/sRNAtoolboxDB/dbs/eukaryotic-tRNAs.fa",
    "tax": "/shared/sRNAtoolboxDB/dbs/taxonomy.txt"
}

QSUB = False
