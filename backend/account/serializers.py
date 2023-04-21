"""This file contains all the serializers for the account app
"""
from rest_framework import serializers
from account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
