"""
This file contains tests for the Profile API.
"""
import pytest
from uuid import uuid4
from django.urls import reverse
from django.contrib.auth.models import User
from account.models import Profile


@pytest.fixture
def init_database():
    """
    This fixture is used to initialize the database with some data.
    """
    # Create User
    user1 = User.objects.create_user(
        username="mario", email="mario@example.com", password="iloveprinces"
    )
    user2 = User.objects.create_user(
        username="luigi", email="luigi@example.com", password="sodoi"
    )

    # Create Profile
    Profile.objects.create(user=user1, username="Mario", email="mario@example.com")
    Profile.objects.create(user=user2, username="Luigi", email="luigi@example.com")


@pytest.mark.django_db
class TestProfileAPI:
    def test_get_all_profiles(self, client, init_database):
        url = reverse("get-all-profiles")
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_get_profile_by_id_on_empty_database_should_raise_DoesNotExist(
        self, client
    ):
        id = uuid4()
        url = reverse("get-one-profile", kwargs={"pk": id})
        with pytest.raises(Profile.DoesNotExist):
            response = client.get(url)
            assert response.status_code == 404

    def test_get_profile_by_id_on_nonempty_database_should_pass(
        self, client, init_database
    ):
        user = User.objects.get(username="mario")
        profile = Profile.objects.get(username="Mario")
        url = reverse("get-one-profile", kwargs={"pk": profile.id})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["username"] == profile.username
        assert response.data["email"] == profile.email
        assert response.data["user"] == user.id
