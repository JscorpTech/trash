from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    FileField,
)

from .base import AbstractBaseModel


class TeamMemberModel(AbstractBaseModel):
    name = CharField(_("Name"), max_length=255)
    picture = FileField(
        _("Picture"), upload_to="team_pictures/", default="team_pictures/default.jpg"
    )
    role = CharField(_("Role"), max_length=255)
    about = TextField(_("About"))

    def __str__(self):
        return f"{self.name} - {self.role}"

    class Meta:
        db_table = "team_members"
        verbose_name = _("Team member")
        verbose_name_plural = _("Team members")
        ordering = ["created_at"]
