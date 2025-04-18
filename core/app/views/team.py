from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.team import TeamMemberModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    TeamMemberListSerializer,
    TeamMemberRetrieveSerializer,
    TeamMemberCreateSerializer,
    TeamMemberUpdateSerializer,
)


@extend_schema(tags=["team_members"])
class TeamMemberViewSet(ModelViewSet):
    queryset = TeamMemberModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return TeamMemberCreateSerializer
            case "update" | "partial_update":
                return TeamMemberUpdateSerializer
            case "list":
                return TeamMemberListSerializer
            case "retrieve":
                return TeamMemberRetrieveSerializer
            case _:
                return TeamMemberListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
