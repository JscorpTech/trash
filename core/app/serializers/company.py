from rest_framework.serializers import ModelSerializer
from core.app.models.company import CompanyModel


class CompanyListSerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
            "id",
            "email",
            "phone",
            "latitude",
            "longitude",
            "projects",
            "staff",
            "work",
            "countries",
        ]


class CompanyRetrieveSerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
            "id",
            "email",
            "phone",
            "latitude",
            "longitude",
            "projects",
            "staff",
            "work",
            "countries",
        ]


class CompanyCreateSerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
            "email",
            "phone",
            "latitude",
            "longitude",
            "projects",
            "staff",
            "work",
            "countries",
        ]


class CompanyUpdateSerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = [
            "email",
            "phone",
            "latitude",
            "longitude",
            "projects",
            "staff",
            "work",
            "countries",
        ]
