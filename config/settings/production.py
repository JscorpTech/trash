from .common import *  # noqa

DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com", "charmes.uz"]
CSRF_TRUSTED_ORIGINS = [env("CSRF_TRUSTED_ORIGINS")]
