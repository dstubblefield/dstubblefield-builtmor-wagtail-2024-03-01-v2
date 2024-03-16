from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-l8_gwl=sedsb(1$d8=kh!8senn(f&1*g##mu98j)6@buue8p!w"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, '.cache'),
    }
}

try:
    from .local import *
except ImportError:
    pass
