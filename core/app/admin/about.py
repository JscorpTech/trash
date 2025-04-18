from django.contrib import admin
from core.app.models.about import AboutModel


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)
