from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.company import CompanyModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    CompanyListSerializer,
    CompanyRetrieveSerializer,
    CompanyCreateSerializer,
    CompanyUpdateSerializer,
)


@extend_schema(tags=["companies"])
class CompanyViewSet(ModelViewSet):
    queryset = CompanyModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return CompanyCreateSerializer
            case "update" | "partial_update":
                return CompanyUpdateSerializer
            case "list":
                return CompanyListSerializer
            case "retrieve":
                return CompanyRetrieveSerializer
            case _:
                return CompanyListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
