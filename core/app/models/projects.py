from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    TextField,
    DecimalField,
    DateField,
    ManyToManyField,
)

from .base import AbstractBaseModel
from .services import PictureModel


class ProjectCategoryModel(AbstractBaseModel):
    name = CharField(_("Name"), max_length=255)


class ProjectModel(AbstractBaseModel):
    name = CharField(_("Name"), max_length=255)
    category = ManyToManyField(
        ProjectCategoryModel, blank=True, verbose_name=_("Category")
    )
    client = CharField(_("Client"), max_length=255)
    architect = CharField(_("Architect"), max_length=255)
    location = CharField(_("Location"), max_length=255)
    size = DecimalField(_("Size (SF)"), max_digits=16, decimal_places=2)
    completed_at = DateField(_("Completed at"))
    about = TextField(_("About"))
    picture = ManyToManyField(PictureModel, blank=True, verbose_name=_("Picture"))
