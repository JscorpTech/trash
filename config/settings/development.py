from .common import *  # noqa
from config.env import env

DEBUG = True
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [env("CSRF_TRUSTED_ORIGINS")]
