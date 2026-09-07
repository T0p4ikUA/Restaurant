from .base import *
import os


DEBUG = False

ALLOWED_HOSTS = ["restaurant-v16h.onrender.com", ".onrender.com", "127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": int(os.environ["POSTGRES_DB_PORT"]),
    }
}

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "HOST": os.environ.get("EMAIL_HOST", "smtp.gmail.com"),
        "PORT": int(os.environ.get("EMAIL_PORT", 587)),
        "HOST_USER": os.environ.get("EMAIL_HOST_USER", ""),
        "HOST_PASSWORD": os.environ.get("EMAIL_HOST_PASSWORD", ""),
        "USE_TLS": True,
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True