from django.contrib import admin
from core.app.models.news import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)
