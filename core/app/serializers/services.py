from rest_framework.serializers import ModelSerializer
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
    class Meta:
        model = ServiceModel
        fields = ["id", "descritpion", "picture"]


class ServiceRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ["id", "descritpion", "picture"]


class ServiceCreateSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ["descritpion", "picture"]


class ServiceUpdateSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ["descritpion", "picture"]
