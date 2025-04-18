from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models.services import PictureModel, ServiceModel


@admin.register(PictureModel)
class PictureAdmin(ModelAdmin):
    list_display = ("id", "created_at")
    ordering = ("-created_at",)


@admin.register(ServiceModel)
class ServiceAdmin(ModelAdmin):
    list_display = ("id", "descritpion", "created_at")
    search_fields = ("descritpion",)
    ordering = ("-created_at",)
