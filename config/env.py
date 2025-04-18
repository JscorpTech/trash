import os
import environ

environ.Env.read_env(os.path.join(".env"))

env = environ.Env(
    # Debugging
    DEBUG=(bool, False),
    # Caching
    CACHE_TIME=(int, 180),
    CACHE_TIMEOUT=(int, 120),
    CACHE_ENABLED=(bool, False),
    # OTP Settings
    OTP_EXPIRE_TIME=(int, 2),
    # Security & Hosts
    ALLOWED_HOSTS=(str, "localhost"),
    CSRF_TRUSTED_ORIGINS=(str, "localhost"),
    # Django Configuration
    DJANGO_SETTINGS_MODULE=(str, "config.settings.development"),
    # Bot Configuration
    BOT_TOKEN=(str, "TOKEN"),
    # Database
    POSTGRES_DB=(str, "db"),
    POSTGRES_USER=(str, "root"),
    POSTGRES_PASSWORD=(str, "password"),
    POSTGRES_HOST=(str, "db"),
)
