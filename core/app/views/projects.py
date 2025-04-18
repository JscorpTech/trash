from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.projects import ProjectModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    ProjectListSerializer,
    ProjectRetrieveSerializer,
    ProjectCreateSerializer,
    ProjectUpdateSerializer,
)


@extend_schema(tags=["projects"])
class ProjectViewSet(ModelViewSet):
    queryset = ProjectModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return ProjectCreateSerializer
            case "update" | "partial_update":
                return ProjectUpdateSerializer
            case "list":
                return ProjectListSerializer
            case "retrieve":
                return ProjectRetrieveSerializer
            case _:
                return ProjectListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
