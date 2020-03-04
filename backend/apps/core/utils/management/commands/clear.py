import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command remove assets files"""

    help = "Remove assets files"

    def handle(self, *args, **options):
        try:
            shutil.rmtree(settings.DIST_DIR)
            for root, folders, files in os.walk(settings.PUBLIC_STATIC_DIR):
                for file in files:
                    if file != ".gitignore":
                        os.remove(os.path.join(root, file))
                for folder in folders:
                    shutil.rmtree(os.path.join(root, folder))
        except FileNotFoundError:
            pass
