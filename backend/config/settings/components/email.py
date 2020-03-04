"""Email settings"""

from config.settings.base import env

EMAIL_CONFIG = env.email_url(
    "EMAIL_URL", default="smtp+ssl://user:password@localhost:25"
)
EMAIL_SUBJECT_PREFIX = ""
SERVER_EMAIL = env("EMAIL_NAME", default="no-reply@localhost")
DEFAULT_FROM_EMAIL = env("EMAIL_NAME", default="no-reply@localhost")
MANAGERS = [
    ("Manager", env("EMAIL_MANAGER", default="manager@localhost")),
]

vars().update(EMAIL_CONFIG)
