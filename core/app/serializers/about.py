from rest_framework.serializers import ModelSerializer
from core.app.models.about import AboutModel


class AboutListSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["id", "title", "short_derscription", "description"]


class AboutRetrieveSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["id", "title", "short_derscription", "description"]


class AboutCreateSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["title", "short_derscription", "description"]


class AboutUpdateSerializer(ModelSerializer):
    class Meta:
        model = AboutModel
        fields = ["title", "short_derscription", "description"]
