from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RegistryConfig(AppConfig):
    """Default app config"""

    name = "apps.api.registry"
    verbose_name = _("Registry")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
