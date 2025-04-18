import re

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from rest_framework.serializers import (
    CharField,
    Serializer,
    ValidationError,
    ChoiceField,
)

User = get_user_model()


from core.app.choices import RoleChoice


class LoginSerializer(Serializer):
    phone = CharField(max_length=20)
    password = CharField(write_only=True)

    def validate_phone(self, value):
        if not re.match(
            r"^(998)(90|91|50|92|93|94|95|96|97|98|99|33|88|77)[0-9]{7}$",
            value,
        ):
            raise ValidationError(_("Phone number is not valid!"))

        if not User.objects.filter(phone=value).exists():
            raise ValidationError(_("There is no user with this phone number!"))

        return value

    def validate(self, attrs):
        phone = attrs.get("phone")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise ValidationError(
                {"phone": _("There is no user with this phone number!")}
            )

        if not user.check_password(password):
            raise ValidationError({"password": _("Incorrect password!")})

        attrs["user"] = user
        return attrs


class RefreshSerializer(TokenRefreshSerializer):
    refresh = CharField(write_only=True)

    def validate(self, attrs):
        refresh = attrs.get("refresh")

        try:
            token = RefreshToken(refresh)
            user = User.objects.get(id=token["user_id"])
        except Exception:
            raise AuthenticationFailed("Invalid or expired refresh token")

        if not user.is_active:
            raise AuthenticationFailed("User account is disabled")

        return {
            "access": str(token.access_token),
            "refresh": str(token),
            "user_id": user.id,
        }


class RegisterSerializer(Serializer):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    phone = CharField(max_length=20)
    password = CharField(write_only=True)
    role = ChoiceField(choices=RoleChoice.choices)

    def validate_phone(self, value):
        if not re.match(
            r"^(998)(90|91|50|92|93|94|95|96|97|98|99|33|88|77)[0-9]{7}$",
            value,
        ):
            raise ValidationError(_("Phone number is not valid!"))

        if User.objects.filter(phone=value).exists():
            raise ValidationError(_("Phone number already registered!"))

        return value

    def create(self, validated_data):
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
            role=validated_data["role"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
