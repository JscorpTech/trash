from rest_framework.serializers import ModelSerializer
from core.app.models.news import NewsModel


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title", "descripiton", "picture"]


class NewsRetrieveSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title", "descripiton", "picture"]


class NewsCreateSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["title", "descripiton", "picture"]


class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["title", "descripiton", "picture"]
