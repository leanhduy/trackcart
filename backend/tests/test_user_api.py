"""
This file contains tests for the User API for the built-in django.contrib.auth.models.User model.
"""
import pytest
from django.urls import reverse
from django.contrib.auth.models import User


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


@pytest.mark.django_db
class TestUserAPI:
    def test_get_all_users(self, client, init_database):
        url = reverse("get-all-users")
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_get_user_by_id_on_empty_database_should_raise_DoesNotExist(self, client):
        url = reverse("get-one-user", kwargs={"pk": 1})
        with pytest.raises(User.DoesNotExist):
            response = client.get(url)
            assert response.status_code == 404

    def test_get_user_by_id_on_nonempty_database_should_pass(
        self, client, init_database
    ):
        user = User.objects.get(username="mario")
        url = reverse("get-one-user", kwargs={"pk": user.id})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["username"] == user.username
        assert response.data["email"] == user.email

    def test_get_user_by_id_access_password_should_raise_KeyError(
        self, client, init_database
    ):
        user = User.objects.get(username="mario")
        url = reverse("get-one-user", kwargs={"pk": user.id})
        response = client.get(url)
        assert response.status_code == 200
        with pytest.raises(KeyError):
            assert response.data["password"]
