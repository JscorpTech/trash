from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models import UserModel
from core.app.permissions import NopePermission
from core.app.utilities import BaseViewSetMixin
from core.app.serializers import (
    UserListSerializer,
    UserRetrieveSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
)


@extend_schema(tags=["users"])
class UserViewSet(ModelViewSet, BaseViewSetMixin):
    queryset = UserModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return UserCreateSerializer
            case "update" | "partial_update":
                return UserUpdateSerializer
            case "list":
                return UserListSerializer
            case "retrieve":
                return UserRetrieveSerializer
            case _:
                return UserListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
