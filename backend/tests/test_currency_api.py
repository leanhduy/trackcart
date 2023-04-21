"""
This file contains the test class to test the Currency API.
"""
import pytest
from django.urls import reverse
from tracker.models import Currency


@pytest.fixture
def init_database():
    """This fixture is used to initialize the database with some data."""
    Currency.objects.create(name="Vietnam Dong", iso="VND")


@pytest.mark.django_db
class TestCurrencyAPI:
    def test_get_all_currencies(self, client):
        url = reverse("get-all-currencies")
        response = client.get(url)
        assert response.status_code == 200

    def test_get_one_currency_empty_database_should_raise_DoesNotExist(self, client):
        url = reverse("get-one-currency", kwargs={"pk": 1})
        with pytest.raises(Currency.DoesNotExist):
            response = client.get(url)

    def test_get_one_currency_should_return_one_currency(self, client, init_database):
        url = reverse("get-one-currency", kwargs={"pk": 1})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["iso"] == "VND"
