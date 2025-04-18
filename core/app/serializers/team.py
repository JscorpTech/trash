from rest_framework.serializers import ModelSerializer
from core.app.models.team import TeamMemberModel


class TeamMemberListSerializer(ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = ["id", "name", "role", "about", "picture"]


class TeamMemberRetrieveSerializer(ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = ["id", "name", "role", "about", "picture"]


class TeamMemberCreateSerializer(ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = ["name", "role", "about", "picture"]


class TeamMemberUpdateSerializer(ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = ["name", "role", "about", "picture"]
