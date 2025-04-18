from django.contrib import admin
from core.app.models.projects import ProjectCategoryModel, ProjectModel


@admin.register(ProjectCategoryModel)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
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
