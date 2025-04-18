from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from core.app.models.news import NewsModel
from core.app.permissions import NopePermission
from core.app.serializers import (
    NewsListSerializer,
    NewsRetrieveSerializer,
    NewsCreateSerializer,
    NewsUpdateSerializer,
)


@extend_schema(tags=["news"])
class NewsViewSet(ModelViewSet):
    queryset = NewsModel.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "create":
                return NewsCreateSerializer
            case "update" | "partial_update":
                return NewsUpdateSerializer
            case "list":
                return NewsListSerializer
            case "retrieve":
                return NewsRetrieveSerializer
            case _:
                return NewsListSerializer

    def get_permissions(self):
        perms = []
        match self.action:
            case "retrieve" | "list":
                perms.extend([AllowAny])
            case _:
                perms.extend([NopePermission])
        self.permission_classes = perms
        return [permission() for permission in self.permission_classes]
