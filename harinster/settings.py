"""
Django settings for harinster project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# from decouple import config
# import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v7657tr#feman4_3o2(!ruqty3dcmx*bn23-a^klvm1e!0yo!3'
# SECRET_KEY = config('SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
#DEBUG = config('DEBUG', default=False, cast=bool) 

ALLOWED_HOSTS = ['harinster.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django_adminlte',
    'django_adminlte_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'order',
    'newsletter',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'harinster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'harinster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# HEROKU DATABASE CONFIG
# DATABASES = { 'default':
# dj_database_url.config( default=config('DATABASE_URL') ) }

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))




# ------------------ static files ----------------------
#STATICFILES_DIRS = (
 #    os.path.join(PROJECT_ROOT, 'static'),
# )

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#---------------------------------------------------------


AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'order:dashboard'
LOGOUT_REDIRECT_URL = 'order:home'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CRISPY_TEMPLATE_PACK = 'bootstrap4'