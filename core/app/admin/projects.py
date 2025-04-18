from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models.projects import ProjectCategoryModel, ProjectModel


@admin.register(ProjectCategoryModel)
class ProjectCategoryAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(ProjectModel)
class ProjectAdmin(ModelAdmin):
    list_display = (
        "name",
        "client",
        "architect",
        "location",
        "size",
        "completed_at",
        "created_at",
    )
    search_fields = ("name", "client", "architect", "location")
    list_filter = ("completed_at",)
    ordering = ("-created_at",)
