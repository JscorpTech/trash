from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models.gallery import GalleryModel


@admin.register(GalleryModel)
class GalleryAdmin(ModelAdmin):
    list_display = ("title", "picture")
    search_fields = ("title",)
    ordering = ("-created_at",)
