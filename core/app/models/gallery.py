from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    FileField,
)

from .base import AbstractBaseModel


class GalleryModel(AbstractBaseModel):
    title = CharField(_("Name"), max_length=255)
    picture = FileField(_("Picture"), upload_to="gallery/")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "gallery"
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")
        ordering = ["created_at"]
