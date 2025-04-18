from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db.models import (  # noqa
    CharField,
    DateTimeField,
    BooleanField,
    ImageField,
    DecimalField,
)
from core.app.choices import RoleChoice
from core.app.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    phone = CharField(_("Phone number"), max_length=20, unique=True)
    first_name = CharField(_("First Name"), max_length=50)
    last_name = CharField(_("Last Name"), max_length=50)

    role = CharField(
        _("Role"), max_length=255, choices=RoleChoice, default=RoleChoice.USER
    )

    is_active = BooleanField(_("Active"), default=True)
    is_staff = BooleanField(_("Staff status"), default=False)

    updated_at = DateTimeField(_("Updated at"), auto_now=True)
    validated_at = DateTimeField(_("Validated at"), null=True, blank=True)
    created_at = DateTimeField(_("Created at"), auto_now_add=True)

    USERNAME_FIELD = "phone"
    objects = UserManager()

    def __str__(self):
        return self.phone

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            phone="9981234567",
            role=RoleChoice.USER,
        )

    @classmethod
    def _create_fake_admin(cls):
        return cls.objects.create(
            phone="1239998877",
            role=RoleChoice.ADMIN,
        )

    class Meta:
        db_table = "users"
        verbose_name = _("User Model")
        verbose_name_plural = _("User Models")
        ordering = ["created_at"]
