from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField

# from core.apps.accounts.choices import AuthProviderChoice, RoleChoice


class BaseUserSerilizer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "role",
            "password",
        ]


class UserListSerializer(BaseUserSerilizer):
    class Meta(BaseUserSerilizer.Meta): ...


class UserRetrieveSerializer(BaseUserSerilizer):
    class Meta(BaseUserSerilizer.Meta): ...


class UserCreateSerializer(BaseUserSerilizer):
    class Meta(BaseUserSerilizer.Meta): ...


class UserUpdateSerializer(BaseUserSerilizer):
    class Meta(BaseUserSerilizer.Meta): ...
