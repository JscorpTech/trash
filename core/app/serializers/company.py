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
            "about_us_title",
            "about_us_short",
            "about_us_description",
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
            "about_us_title",
            "about_us_short",
            "about_us_description",
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
            "about_us_title",
            "about_us_short",
            "about_us_description",
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
            "about_us_title",
            "about_us_short",
            "about_us_description",
        ]
