from rest_framework.serializers import ModelSerializer
from core.app.models.news import NewsModel


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title", "short_description", "description", "picture"]


class NewsRetrieveSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title", "short_description", "description", "picture"]


class NewsCreateSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["title", "short_description", "description", "picture"]


class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["title", "short_description", "description", "picture"]
