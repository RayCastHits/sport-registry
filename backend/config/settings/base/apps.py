DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "import_export",
    "corsheaders",
    "widget_tweaks",
    "rest_framework",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "webpack_loader",
    "etc",
    "drf_multiple_model",
    "constance",
    "constance.backends.database",
    "hijack",
    "compat",
    "hijack_admin",
]

PROJECT_APPS = [
    "apps.core.utils",
    "apps.core.main",
    "apps.core.api",
    "apps.api.auth",
    "apps.api.registry",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
]
