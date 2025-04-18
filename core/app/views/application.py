from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.application import ApplicationModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    ApplicationListSerializer,
    ApplicationRetrieveSerializer,
    ApplicationCreateSerializer,
    ApplicationUpdateSerializer,
)


@extend_schema(tags=["applications"])
class ApplicationViewSet(ModelViewSet):
    queryset = ApplicationModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return ApplicationCreateSerializer
            case "update" | "partial_update":
                return ApplicationUpdateSerializer
            case "list":
                return ApplicationListSerializer
            case "retrieve":
                return ApplicationRetrieveSerializer
            case _:
                return ApplicationListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]
