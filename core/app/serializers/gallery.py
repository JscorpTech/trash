from rest_framework.serializers import ModelSerializer, CharField

# from core.apps.accounts.choices import AuthProviderChoice, RoleChoice
from core.app.models import GalleryModel


class BaseGallerySerilizer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = GalleryModel
        fields = [
            "id",
            "title",
            "picture",
        ]


class GalleryListSerializer(BaseGallerySerilizer):
    class Meta(BaseGallerySerilizer.Meta): ...


class GalleryRetrieveSerializer(BaseGallerySerilizer):
    class Meta(BaseGallerySerilizer.Meta): ...


class GalleryCreateSerializer(BaseGallerySerilizer):
    class Meta(BaseGallerySerilizer.Meta): ...


class GalleryUpdateSerializer(BaseGallerySerilizer):
    class Meta(BaseGallerySerilizer.Meta): ...
