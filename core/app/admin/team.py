from django.contrib import admin
from unfold.admin import ModelAdmin
from core.app.models.team import TeamMemberModel


@admin.register(TeamMemberModel)
class TeamMemberAdmin(ModelAdmin):
    list_display = ("name", "role", "created_at")
    search_fields = ("name", "role")
    ordering = ("-created_at",)
