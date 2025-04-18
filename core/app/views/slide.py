from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.slide import SlideModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    SlideListSerializer,
    SlideRetrieveSerializer,
    SlideCreateSerializer,
    SlideUpdateSerializer,
)


@extend_schema(tags=["slides"])
class SlideViewSet(ModelViewSet):
    queryset = SlideModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return SlideCreateSerializer
            case "update" | "partial_update":
                return SlideUpdateSerializer
            case "list":
                return SlideListSerializer
            case "retrieve":
                return SlideRetrieveSerializer
            case _:
                return SlideListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
