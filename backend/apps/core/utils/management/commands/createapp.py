import os

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Command create django app"""

    help = (
        "Creates a Django app directory structure"
        " for the given app name in the apps directory."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "name", type=str, help="Name of the application or project"
        )
        parser.add_argument(
            "--api",
            default=False,
            action="store_true",
            help="Create app in folder api",
        )
        parser.add_argument(
            "--core",
            default=False,
            action="store_true",
            help="Create app in folder core",
        )

    def handle(self, *args, **options):
        name = options["name"]
        is_api = options["api"]
        is_core = options["core"]
        path = settings.APPS_DIR
        template = settings.DEFAULT_APP_TEMPLATE

        if is_api and is_core:
            raise CommandError("--api and --core can't be used together")
        if is_api:
            path = os.path.join(path, "api")
            template = settings.API_APP_TEMPLATE
            if not os.path.exists(path):
                raise CommandError("Package api is not exist")
        if is_core:
            path = os.path.join(path, "core")
            template = settings.CORE_APP_TEMPLATE
            if not os.path.exists(path):
                raise CommandError("Package core is not exist")
        path = os.path.join(path, name)
        if not os.path.exists(path):
            os.mkdir(path)
        management.call_command(
            "startapp", name, path, f"--template={template}"
        )
