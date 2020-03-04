from django.contrib import admin
from django.contrib.auth.models import Group as BaseGroup
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from hijack_admin.admin import HijackUserAdminMixin

from apps.core.utils.admin import BaseAdminMixin
from .models import User, ProxyGroup


@admin.register(User)
class UserAdmin(BaseAdminMixin, HijackUserAdminMixin, BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "hijack_field",
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)
