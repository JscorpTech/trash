from rest_framework.serializers import ModelSerializer
from core.app.models.application import ApplicationModel


class ApplicationListSerializer(ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ["id", "name", "email", "subject", "message"]


class ApplicationRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ["id", "name", "email", "subject", "message"]


class ApplicationCreateSerializer(ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ["name", "email", "subject", "message"]


class ApplicationUpdateSerializer(ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = ["name", "email", "subject", "message"]
