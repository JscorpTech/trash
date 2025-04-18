from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models import UserModel


@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    list_display = (
        "phone",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "is_staff",
    )
    search_fields = [
        "phone",
    ]
    list_filter = ("is_staff", "is_active", "role")
