from rest_framework import serializers
from rest_framework.views import APIView
from collect.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id' 'username', 'profile_picture', 'bio', 'contact')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'title', 'image', 'decription', 'link', 'user',)
