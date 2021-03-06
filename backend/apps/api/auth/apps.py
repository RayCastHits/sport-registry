from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthConfig(AppConfig):
    """Default app config"""

    label = "auth_api"
    name = "apps.api.auth"
    verbose_name = _("Authentication and Authorization")
