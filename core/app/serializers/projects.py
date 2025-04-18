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

    def get_picture(self, obj):
        request = self.context.get("request")
        pics = obj.picture.all()
        urls = []
        for pic in pics:
            if pic.picture:
                if request:
                    urls.append(request.build_absolute_uri(pic.picture.url))
                else:
                    urls.append(pic.picture.url)
        return urls


class ProjectRetrieveSerializer(ModelSerializer):
    picture = SerializerMethodField()

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

    def get_picture(self, obj):
        request = self.context.get("request")
        pics = obj.picture.all()
        urls = []
        for pic in pics:
            if pic.picture:
                if request:
                    urls.append(request.build_absolute_uri(pic.picture.url))
                else:
                    urls.append(pic.picture.url)
        return urls


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
