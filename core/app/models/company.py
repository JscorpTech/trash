from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CharField,
    DecimalField,
    EmailField,
    PositiveIntegerField,
    TextField,
)

from .base import AbstractBaseModel


class CompanyModel(AbstractBaseModel):
    email = EmailField(_("Email"))
    phone = CharField(_("Phone number"), max_length=20)
    latitude = DecimalField(_("Location latitude"), max_digits=10, decimal_places=7)
    longitude = DecimalField(_("Location longitude"), max_digits=10, decimal_places=7)

    projects = PositiveIntegerField(_("Number of projects"))
    staff = PositiveIntegerField(_("Number of employees"))
    work = PositiveIntegerField(_("Hours of work "))
    countries = PositiveIntegerField(_("Countries"))
    about_us_title = CharField(_("About us title"), max_length=255)
    about_us_description = TextField(_("About us description"))

    def __str__(self):
        return f"{self.email} - {self.phone}"

    class Meta:
        db_table = "company"
        verbose_name = _("Company")
        verbose_name_plural = _("Company")
        ordering = ["created_at"]
