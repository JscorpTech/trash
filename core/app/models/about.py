from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, TextField

from .base import AbstractBaseModel
from core.app.choices import TitleChoice


class AboutModel(AbstractBaseModel):
    title = CharField(_("Title"), choices=TitleChoice, max_length=255)
    descripiton = TextField(_("Description"), max_length=255)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "about"
        verbose_name = _("About")
        verbose_name_plural = _("About")
        ordering = ["created_at"]
