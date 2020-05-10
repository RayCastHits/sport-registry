from django.contrib import admin
from . import models

# from .models import Sportsman


# class SportsmanAdmin(admin.ModelAdmin):
#     list_display = ["name"]


# admin.site.register(Sportsman, SportsmanAdmin)


class ParentInline(admin.TabularInline):
    model = models.Parent
    max_num = 2


class SportsmanAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        ParentInline,
    ]


admin.site.register(models.Sportsman, SportsmanAdmin)
