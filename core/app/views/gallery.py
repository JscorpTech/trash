from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.gallery import GalleryModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    GalleryListSerializer,
    GalleryRetrieveSerializer,
    GalleryCreateSerializer,
    GalleryUpdateSerializer,
)


@extend_schema(tags=["gallery"])
class GalleryViewSet(ModelViewSet):
    queryset = GalleryModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return GalleryCreateSerializer
            case "update" | "partial_update":
                return GalleryUpdateSerializer
            case "list":
                return GalleryListSerializer
            case "retrieve":
                return GalleryRetrieveSerializer
            case _:
                return GalleryListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
