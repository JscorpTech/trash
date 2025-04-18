from rest_framework.serializers import ModelSerializer
from core.app.models.about import AboutModel


class AboutListSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["id", "title", "descripiton"]


class AboutRetrieveSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["id", "title", "descripiton"]


class AboutCreateSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["title", "descripiton"]


class AboutUpdateSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["title", "descripiton"]
