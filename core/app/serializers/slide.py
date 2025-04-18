from rest_framework.serializers import ModelSerializer
from core.app.models.slide import SlideModel


class SlideListSerializer(ModelSerializer):
    class Meta:
        model = SlideModel
        fields = ["id", "title", "descripiton", "slide"]


class SlideRetrieveSerializer(ModelSerializer):
    class Meta:
        model = SlideModel
        fields = ["id", "title", "descripiton", "slide"]


class SlideCreateSerializer(ModelSerializer):
    class Meta:
        model = SlideModel
        fields = ["title", "descripiton", "slide"]


class SlideUpdateSerializer(ModelSerializer):
    class Meta:
        model = SlideModel
        fields = ["title", "descripiton", "slide"]
