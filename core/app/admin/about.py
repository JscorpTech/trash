from django.contrib import admin
from core.app.models.about import AboutModel
from unfold.admin import ModelAdmin


@admin.register(AboutModel)
class AboutAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)
