from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class RoleChoice(TextChoices):

    ADMIN = "admin", _("Admin")
    OWNER = "owner", _("Owner")
    MANAGER = "manager", _("Manager")
    USER = "user", _("User")


class LanguageChoice(TextChoices):

    UZBEK = "lang_uz", _("Uzbek")
    RUSSIAN = "lang_ru", _("Russian")
    ENGLISH = "lang_en", _("English")
