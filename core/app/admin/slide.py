from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models.slide import SlideModel


@admin.register(SlideModel)
class SlideAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)
