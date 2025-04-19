from rest_framework.serializers import ModelSerializer
from core.app.models.about import AboutModel


class AboutListSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["id", "title", "short_description", "description"]


class AboutRetrieveSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["id", "title", "short_description", "description"]


class AboutCreateSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["title", "short_description", "description"]


class AboutUpdateSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["title", "short_description", "description"]
