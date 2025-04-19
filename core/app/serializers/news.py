from rest_framework.serializers import ModelSerializer
from core.app.models.news import NewsModel


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title", "short_derscription", "descritpion", "picture"]


class NewsRetrieveSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title", "short_derscription", "descritpion", "picture"]


class NewsCreateSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["title", "short_derscription", "descritpion", "picture"]


class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["title", "short_derscription", "descritpion", "picture"]
