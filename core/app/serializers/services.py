from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.app.models.services import PictureModel, ServiceModel


class PictureListSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ["id", "picture"]


class PictureRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ["id", "picture"]


class PictureCreateSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ["picture"]


class PictureUpdateSerializer(ModelSerializer):
    class Meta:
        model = PictureModel
        fields = ["picture"]


class ServiceListSerializer(ModelSerializer):
    picture = SerializerMethodField()

    class Meta:
        model = ServiceModel
        fields = ["id", "descritpion", "picture"]

    def get_picture(self, obj):
        request = self.context.get("request")
        return [
            request.build_absolute_uri(p.picture.url)
            for p in obj.picture.all()
            if p.picture
        ]


class ServiceRetrieveSerializer(ModelSerializer):
    picture = SerializerMethodField()

    class Meta:
        model = ServiceModel
        fields = ["id", "descritpion", "picture"]

    def get_picture(self, obj):
        request = self.context.get("request")
        return [
            request.build_absolute_uri(p.picture.url)
            for p in obj.picture.all()
            if p.picture
        ]


class ServiceCreateSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ["descritpion", "picture"]


class ServiceUpdateSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ["descritpion", "picture"]
