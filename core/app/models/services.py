from django.utils.translation import gettext_lazy as _
from django.db.models import TextField, FileField, ManyToManyField, CharField

from .base import AbstractBaseModel


class PictureModel(AbstractBaseModel):
    picture = FileField(upload_to="pictures/")

    def __str__(self):
        return self.picture.name.split("/")[-1]

    class Meta:
        db_table = "news_picture"
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")
        ordering = ["created_at"]


class ServiceModel(AbstractBaseModel):
    title = CharField(_("Title"), max_length=255, default="")
    descritpion = TextField(_("Description"))
    picture = ManyToManyField(
        PictureModel, blank=True, null=True, verbose_name=_("Picture")
    )
