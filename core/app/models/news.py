from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, TextField, FileField

from .base import AbstractBaseModel


class NewsModel(AbstractBaseModel):
    title = CharField(_("Title"), max_length=255)
    descripiton = TextField(_("Description"))
    picture = FileField(upload_to="news/")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "news"
        verbose_name = _("New")
        verbose_name_plural = _("News")
        ordering = ["created_at"]
