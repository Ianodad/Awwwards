from rest_framework import serializers
from rest_framework.views import APIView
from collect.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'profile_picture', 'bio', 'contact')
