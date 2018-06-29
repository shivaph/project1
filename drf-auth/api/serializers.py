from rest_framework import serializers
from Users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.User


class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.MedicalCondition

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Group

class GroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("abbrev",)
        model = models.User
