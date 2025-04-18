from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.about import AboutModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    AboutListSerializer,
    AboutRetrieveSerializer,
    AboutCreateSerializer,
    AboutUpdateSerializer,
)


@extend_schema(tags=["about"])
class AboutViewSet(ModelViewSet):
    queryset = AboutModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return AboutCreateSerializer
            case "update" | "partial_update":
                return AboutUpdateSerializer
            case "list":
                return AboutListSerializer
            case "retrieve":
                return AboutRetrieveSerializer
            case _:
                return AboutListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
