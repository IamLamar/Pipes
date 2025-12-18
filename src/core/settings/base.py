# base.py
# ruff: noqa
from pathlib import Path
import os
import warnings
from dotenv import load_dotenv
from .jazzmin import *
from .cors import *
from decouple import config
from .jazzmin import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
PROD = os.getenv("PROD") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")


JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI = JAZZMIN_UI_TWEAKS

if PROD:
    from .prod import *
else:
    from .dev import *

INSTALLED_APPS = [
    "corsheaders",
    "jazzmin",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "phonenumber_field",
    "rest_framework",
    "django_extensions",
    "django_filters",
    "drf_spectacular",
    "colorfield",
    "ckeditor",
    "apps.mainpage",
    "apps.service_page",
    "apps.products",
    "apps.news",
    "apps.projects",
    "apps.contacts",
    "apps.company",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
ROOT_URLCONF = "core.routes"

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

WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "ru"

LANGUAGES = [("ru", "Russian")]

warnings.filterwarnings(
    "ignore",
    message="django-ckeditor bundles CKEditor 4.22.1 which isn't supported anymore",
    category=UserWarning,
)

STATIC_URL = "/back_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "back_static")


MEDIA_URL = "/back_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "back_media")


REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}

# Email
EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_PORT = config("EMAIL_PORT", cast=int, default=25)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=False)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool, default=False)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="webmaster@localhost")
