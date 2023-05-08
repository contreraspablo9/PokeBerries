"""
Django settings for pokeberries project.

"""
import importlib
import os
from django.core.exceptions import ImproperlyConfigured

#
# Configuration import
#

# for custom configuration add custom config file path on env variables
config_path = os.getenv("POKEBERRIES_CONFIGURATION", "pokeberries.base_configuration")
try:
    configuration = importlib.import_module(config_path)
except ModuleNotFoundError as e:
    if getattr(e, "name") == config_path:
        raise ImproperlyConfigured(
            f"Specified configuration module ({config_path}) not found. "
            f"Please define pokeberries/pokeberries/base_configuration.py "
            f"per the documentation, or specify an alternate module in the "
            f"POKEBERRIES_CONFIGURATION environment variable."
        )
    raise

# Set required parameters
ALLOWED_HOSTS = getattr(configuration, "ALLOWED_HOSTS")
BASE_DIR = getattr(configuration, "BASE_DIR")
BASE_PATH = getattr(configuration, "BASE_PATH", "")
DATABASE = getattr(configuration, "DATABASE")
DEBUG = getattr(configuration, "DEBUG", True)
DEFAULT_LANGUAGE = getattr(configuration, "DEFAULT_LANGUAGE", "en-us")
ENVIRONMENT = getattr(configuration, "ENVIRONMENT")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5cp1^8l6w=c0adyb3r)=)(cj4zjh!0n%6!c_ccx#=0jp%3vxe)"

# Application definition

INSTALLED_APPS = [
    "berries",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pokeberries.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pokeberries.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {"default": DATABASE}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
