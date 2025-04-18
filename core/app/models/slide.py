from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    FileField,
)

from .base import AbstractBaseModel


class SlideModel(AbstractBaseModel):
    title = CharField(_("Title"), max_length=255)
    descripiton = TextField(_("Description"))
    slide = FileField(upload_to="slides/")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "slides"
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")
        ordering = ["created_at"]
