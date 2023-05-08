"""POKEBERRIES BASE CONFIGURATION MODULE"""

import os
from pathlib import Path

ALLOWED_HOSTS = ["*"]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Base URL path if accessing PokeBerries within a directory. For example, if installed at https://example.com/pokeberries/, set:
# BASE_PATH = 'pokeberries/'
BASE_PATH = ""

# PostgreSQL database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASE = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv("POKEBERRIES_DB_NAME"),            # Database name
    'USER': os.getenv("POKEBERRIES_DB_USERNAME"),        # PostgreSQL username
    'PASSWORD': os.getenv("POKEBERRIES_DB_PASSWORD"),    # PostgreSQL password
    'HOST': os.getenv("POKEBERRIES_DB_HOST"),            # Database server
    'PORT': os.getenv("POKEBERRIES_DB_PORT"),            # Database port (leave blank for default)
    'CONN_MAX_AGE': 300,                                 # Max database connection age
}

# Environment name
ENVIRONMENT = os.getenv("ENVIRONMENT", "local_sandbox")

# Set to True to enable server debugging. WARNING: Debugging introduces a substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while performing testing. Never enable debugging
# on a production system.
DEBUG = (ENVIRONMENT != "production")

# Set the default preferred language/locale
DEFAULT_LANGUAGE = 'en-us'
