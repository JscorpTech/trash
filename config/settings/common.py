import os
from pathlib import Path
from config.env import env
from config.conf import *  # noqa
from django.utils.translation import gettext_lazy as _
# import dj_database_url

# from config.conf.unfold import UNFOLD  # noqa

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Security
SECRET_KEY = env("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["charmes.uz"]

LANGUAGE_CODE = "en"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ("uz", _("Uzbek")),
    ("ru", _("Russia")),
    ("en", _("English")),
)
# Installed Apps
INSTALLED_APPS = PROJECT_APPS + THIRD_PARTY_APPS + DEFAULT_APSS

# ADMIN_SITE = "config.conf.admin.admin_site"
# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Authentication
AUTH_USER_MODEL = "app.UserModel"

# URLs & WSGI/ASGI
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# Templates
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


# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Static Files
STATIC_URL = "/backend/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "resources/static")

# Media
MEDIA_URL = "/backend/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "resources/media")

# Default Primary Key Field Type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}
# DATABASES = {
#     "default": dj_database_url.config(
#         default=env("DATABASE_URL"),
#         conn_max_age=600,  # Optional: Sets the maximum age of persistent database connections
#         ssl_require=True,  # Optional: Whether SSL is required for the connection
#     )
# }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}
