from django.contrib import admin
from . import models

# from .models import Sportsman


# class SportsmanAdmin(admin.ModelAdmin):
#     list_display = ["name"]


# admin.site.register(Sportsman, SportsmanAdmin)


class ParentInline(admin.TabularInline):
    model = models.Parent
    max_num = 2


class ParentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    # max_num = 2


admin.site.register(models.Parent, ParentAdmin)


class SportsmanAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "patronymic", "gender"]
    inlines = [
        ParentInline,
    ]


admin.site.register(models.Sportsman, SportsmanAdmin)


class SportTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(models.SportType, SportTypeAdmin)


class RankAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(models.Rank, RankAdmin)


class PrimaryAdmin(admin.ModelAdmin):
    list_display = [
        "sportsman",
    ]


admin.site.register(models.Primary, PrimaryAdmin)


class MedicalAdmin(admin.ModelAdmin):
    list_display = [
        "sportsman",
    ]


admin.site.register(models.Medical, MedicalAdmin)


class SportResultAdmin(admin.ModelAdmin):
    list_display = [
        "result",
    ]


admin.site.register(models.SportResult, SportResultAdmin)
