"""
Django settings for Social_system project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tnxyjc%l%bdo!ov66=5!acgsqg(pkr%#^l=kksv8soh-knq9k$')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)
ALLOWED_HOST = '.onrender.com'
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS','127.0.0.1') ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'autification', 
    'social',
    'tinymce',
    'cloudinary',
    'cloudinary_storage',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Social_system.urls'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Social_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL='/media/'
MEDIA_ROOT = BASE_DIR /'media'

LOGIN_REDIRECT_URL = 'communities'
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = LOGIN_URL

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL='/media/'

CLOUDINARY_STORAGE = {
    'NAME':'den9yj6z5',
    'API_KEY':'498996848524315',
    'API_SECRET':'kWT8gvHt4tffDaRQPqv0SADQ5bE'
}

# # TINYMCE_JS_ROOT = os.path.join(BASE_DIR, 'static/js/tiny_mce/')
# # TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
# TINYMCE_DEFAULT_CONFIG = {
#     "height": "320px",
#     "width": "960px",
#     "menubar": "file edit view insert format tools table help",
#     "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
#     "fullscreen insertdatetime media table paste code help wordcount spellchecker",
#     "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
#     "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
#     "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
#     "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
#     "a11ycheck ltr rtl | showcomments addcomment code",
#     "custom_undo_redo_levels": 10,
#     "language": "es_ES",  # To force a specific language instead of the Django current language.
# }
# TINYMCE_SPELLCHECKER = True
# # TINYMCE_COMPRESSOR = True
# TINYMCE_EXTRA_MEDIA = {
#     'css': {
#         'all': [
#             ...
#         ],
#     },
#     'js': [
#         ...
#     ],
# }
