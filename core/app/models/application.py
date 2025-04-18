from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    EmailField,
)

from .base import AbstractBaseModel


class ApplicationModel(AbstractBaseModel):
    name = CharField(_("Name"), max_length=255)
    email = EmailField(_("Email"), max_length=255)
    subject = CharField(_("Subject"), max_length=255)
    message = TextField(_("Message"))

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        db_table = "applications"
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ["created_at"]
