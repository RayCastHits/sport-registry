"""Project settings"""
# flake8: noqa
from config.settings.components import *
from config.settings.environments import *
from config.settings.custom import *

SETTINGS_EXPORT = [
    "DEBUG",
    "LANGUAGE_CODE",
    "TEMPLATE_LAYOUT",
]
