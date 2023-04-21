"""This file contains all the views for the account app
"""
from django.contrib.auth.models import User
from account.models import Profile
from account.serializers import ProfileSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# * USER VIEWS
@api_view(["GET"])
def get_all_users(request):
    """
    This view is used to get all the users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_user(request, pk):
    """
    This view is used to get one user by its uuid
    """
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# * PROFILE VIEWS
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
