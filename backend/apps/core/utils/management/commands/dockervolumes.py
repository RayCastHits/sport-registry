import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command create .docker folder structure"""

    help = "Create .docker folder structure"

    def create(self, path: str):
        """Create path if not exist"""
        if not os.path.exists(path):
            os.makedirs(path)

    def handle(self, *args, **options):
        self.create(settings.DOCKER_DB_DIR)
        self.create(settings.DOCKER_STATIC_DIR)
        self.create(settings.DOCKER_LOG_DIR)
        self.create(settings.DOCKER_MEDIA_DIR)
