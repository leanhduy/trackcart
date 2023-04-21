"""
This file contains the test class to test the Wallet API.
"""
import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from tracker.models import Wallet, Profile, Currency
from account.models import Profile


# Fixtures
@pytest.fixture
def init_database():
    # Create User
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="123"
    )

    # Create Profile
    Profile.objects.create(user=user, username="testuser", email="test@example.com")
    owner = Profile.objects.get(username="testuser")

    # Create Currency
    Currency.objects.create(name="Vietnam Dong", iso="VND")
    Currency.objects.create(name="US Dollar", iso="USD")

    # Create wallets
    Wallet.objects.create(
        name="Test wallet 1",
        balance=1000,
        owner=owner,
        currency=Currency.objects.get(iso="USD"),
    )

    Wallet.objects.create(
        name="Test wallet 2",
        balance=40000000,
        owner=owner,
        currency=Currency.objects.get(iso="VND"),
    )


@pytest.mark.django_db
class TestWalletAPI:
    def test_get_all_wallets(self, client, init_database):
        url = reverse("get-all-wallets")
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_get_wallet_by_id_on_empty_database_should_raise_DoesNotExist(self, client):
        url = reverse("get-one-wallet", kwargs={"pk": 1})
        with pytest.raises(Wallet.DoesNotExist):
            response = client.get(url)
            assert response.status_code == 404

    def test_get_wallet_by_id_on_not_empty_database_should_pass(
        self, client, init_database
    ):
        id = Wallet.objects.get(name="Test wallet 1").id
        url = reverse("get-one-wallet", kwargs={"pk": id})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["name"] == "Test wallet 1"
        assert response.data["balance"] == "1000.00"
