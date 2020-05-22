from django.contrib import admin
from django.contrib.auth.models import Group as BaseGroup
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from hijack_admin.admin import HijackUserAdminMixin
from django.utils.translation import gettext, gettext_lazy as _

from apps.core.utils.admin import BaseAdminMixin
from .models import User, ProxyGroup


@admin.register(User)
class UserAdmin(BaseAdminMixin, HijackUserAdminMixin, BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "patronymic",
        "role",
        "is_staff",
        "hijack_field",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                    "email",
                    "role",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)
