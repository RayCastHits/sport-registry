"""Production settings"""

from config.settings.base import PRODUCTION_APPS, PRODUCTION_MIDDLEWARE, env
from config.settings.components.paths import (
    DEV_DATABASE_FILE,
    TEST_DATABASE_FILE,
)

ALLOWED_HOSTS = [
    env("SITE_DOMAIN"),
]

INSTALLED_APPS = [
    *PRODUCTION_APPS,
]

MIDDLEWARE = [
    *PRODUCTION_MIDDLEWARE,
]

if env("USE_SQLITE", default=False):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": DEV_DATABASE_FILE,
            "TEST": {"NAME": TEST_DATABASE_FILE,},
        },
    }
else:
    DATABASES = {
        "default": env.db(),
    }
