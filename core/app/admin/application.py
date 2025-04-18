from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models.application import ApplicationModel


@admin.register(ApplicationModel)
class ApplicationAdmin(ModelAdmin):  # changed from admin.ModelAdmin to ModelAdmin
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    ordering = ("-created_at",)
