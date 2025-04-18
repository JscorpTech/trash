from django.contrib import admin
from core.app.models.company import CompanyModel


@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "projects",
        "staff",
        "work",
        "countries",
        "created_at",
    )
    search_fields = ("email", "phone")
    ordering = ("-created_at",)
