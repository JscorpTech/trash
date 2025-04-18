from rest_framework.serializers import ModelSerializer
from core.app.models.projects import ProjectCategoryModel, ProjectModel


class ProjectCategoryListSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategoryModel
        fields = ["id", "name"]


class ProjectCategoryRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategoryModel
        fields = ["id", "name"]


class ProjectCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategoryModel
        fields = ["name"]


class ProjectCategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategoryModel
        fields = ["name"]


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "name",
            "category",
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "picture",
        ]


class ProjectRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "name",
            "category",
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "picture",
        ]


class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "name",
            "category",
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "picture",
        ]


class ProjectUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "name",
            "category",
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "picture",
        ]
