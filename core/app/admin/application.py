from django.contrib import admin
from core.app.models.application import ApplicationModel


@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    ordering = ("-created_at",)
