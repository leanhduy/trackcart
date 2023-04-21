"""This file contains all the views for the account app
"""
from django.shortcuts import render
from account.models import Profile
from account.serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def get_all_profiles(request):
    """
    This view is used to get all the profiles.
    """
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_profile(request, pk):
    """
    This view is used to get one profile by its uuid
    """
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)
