from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NetworkConfig(AppConfig):
    """Default app config"""

    name = "apps.api.network"
    verbose_name = _("Network")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
