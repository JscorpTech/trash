from django.db.models import Model, DateTimeField, CharField, BooleanField
from django.utils.translation import gettext_lazy as _


class AbstractBaseModel(Model):
    updated_at = DateTimeField(_("Updated at"), auto_now=True)
    created_at = DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        abstract = True


class BaseDocumentModel(AbstractBaseModel):
    title = CharField(_("Title"), max_length=255, null=True, blank=True)
    is_active = BooleanField(_("Is active"), default=True)

    class Meta:
        abstract = True
