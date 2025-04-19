from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

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
    picture = SerializerMethodField()
    category = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "name",
            "category",  # now returns ["Home construction", "Renovation", …]
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "short_description",
            "picture",
        ]

    def get_picture(self, obj):
        request = self.context.get("request")
        urls = []
        for pic in obj.picture.all():
            if pic.picture:
                url = pic.picture.url
                urls.append(request.build_absolute_uri(url) if request else url)
        return urls


class ProjectRetrieveSerializer(ModelSerializer):
    picture = SerializerMethodField()
    category = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = ProjectModel
        fields = [
            "id",
            "name",
            "category",  # now returns names
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "short_description",
            "picture",
        ]

    def get_picture(self, obj):
        request = self.context.get("request")
        urls = []
        for pic in obj.picture.all():
            if pic.picture:
                url = pic.picture.url
                urls.append(request.build_absolute_uri(url) if request else url)
        return urls


class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "name",
            "category",  # input still accepts IDs
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "short_description",
            "picture",
        ]


class ProjectUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = [
            "name",
            "category",  # input still accepts IDs
            "client",
            "architect",
            "location",
            "size",
            "completed_at",
            "about",
            "short_description",
            "picture",
        ]
