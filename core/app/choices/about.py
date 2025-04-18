from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TitleChoice(TextChoices):
    TITLE_1 = "title_1", _("Charm manufacturing")
    TITLE_2 = "title_2", _("Leather crafting")
    TITLE_3 = "title_3", _("Interior design")
    TITLE_4 = "title_4", _("Exterior design")
    TITLE_5 = "title_5", _("Renovation")
    TITLE_6 = "title_6", _("Safety Management")
