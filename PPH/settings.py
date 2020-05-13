"""
Django settings for PPH project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!i&fuhrq9lo!vafyupr_c0jgqbewpc)%mdebjbeiurl+&mx691'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'KM',
    'USER',
    'WEB',
    'SEARCH',

#third party===============================
    'taggit',
    'ckeditor',
    'bootstrap4',
    'dateutil',
    'crispy_forms',
    'google_analytics',
    'meta',
    'captcha',
    'django_social_share',
    'rangefilter',
    'fullcalendar'
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

ROOT_URLCONF = 'PPH.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'PPH.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
)


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#STATIC_URL          = '/static/'

#if not DEBUG: 
#STATIC_ROOT = '/Users/nurojilukmansyah/Dev/django/PPH/static'

STATICFILES_DIRS    = [ os.path.join(BASE_DIR, 'static/'),]

STATIC_URL          = '/static/'

MEDIA_URL           = '/media/'

MEDIA_ROOT          = os.path.join(BASE_DIR, 'download')

SVG_DIRS            = [os.path.join(BASE_DIR, 'static/svg') ]



#==========================================THIRD PARTY SETTINGS======================================================


#CKEDITOR -----------------------------------------------------------------------------------------------------------
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'width': 'auto',
        'height': 'auto',
    },
}

#Mailchimp ----------------------------------------------------------------------------------------------------------
MAILCHIMP_API_KEY = 'bb96a92e868cae07a049a5d25cf688f4-us20'
MAILCHIMP_DATA_CENTER = 'us20'
MAILCHIMP_EMAIL_LIST_ID = '75b463b1fa'

#CUSTOM USER --------------------------------------------------------------------------------------------------------
AUTH_USER_MODEL = 'USER.CustomUser'

#Redirect URL --------------------------------------------------------------------------------------------------------
LOGIN_REDIRECT_URL = 'KM-Penelitian'
LOGOUT_REDIRECT_URL = 'home-web'

#crispy form --------------------------------------------------------------------------------------------------------
CRISPY_TEMPLATE_PACK ='bootstrap4'

#rechaptha lama -----------------------------------------------------------------------------------------------------
GOOGLE_RECAPTCHA_SECRET_KEY = '6Le0U9IUAAAAAGTnpukJpXl-gZPG9XwBvdFfrVJX'

#google rechaptha ---------------------------------------------------------------------------------------------------
RECAPTCHA_PUBLIC_KEY = '6Ld5zdIUAAAAAEBQ7E4JUlTRpvyv8LwHFYopOCwo'
RECAPTCHA_PRIVATE_KEY = '6Ld5zdIUAAAAAJqieEqW8qF4b5RRO49PShA3lVT5'


#Email------------------------------------------------
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='smtp.gmail.com'
EMAIL_USE_TLS=1
EMAIL_PORT=587
EMAIL_HOST_USER='nurojilukmansyah2@gmail.com'
EMAIL_HOST_PASSWORD='n6dy66m6liy6h'
EMAIL_PORT = 587

DATE_INPUT_FORMATS = ['%d-%m-%Y']