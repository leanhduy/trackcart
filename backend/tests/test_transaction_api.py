"""
This file contains the test class to test the Transaction API.
"""
import pytest
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from tracker.models import Wallet, Profile, Currency, Transaction, Category
from account.models import Profile


# Fixtures
@pytest.fixture
def init_database():
    """This fixture is used to initialize the database with some data."""
    # Create User
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="123"
    )

    # Create Profile
    Profile.objects.create(user=user, username="testuser", email="test@example.com")
    owner = Profile.objects.get(username="testuser")

    # Create Currency
    Currency.objects.create(name="US Dollar", iso="USD")

    # Create wallets
    Wallet.objects.create(
        name="Test wallet 1",
        balance=1000,
        owner=owner,
        currency=Currency.objects.get(iso="USD"),
    )

    # Create category
    Category.objects.create(
        name="Food & Beverage", cate_type="expense", sub_category="required"
    )
    Category.objects.create(name="Salary", cate_type="income", sub_category="income")

    # Create transactions
    Transaction.objects.create(
        name="Cafe with old colleagues",
        amount=3,
        wallet=Wallet.objects.get(name="Test wallet 1"),
        category=Category.objects.get(name="Food & Beverage"),
        date="2023-04-21",
        note="Mylife Coffee",
    )

    Transaction.objects.create(
        name="Dinner",
        amount=6.75,
        wallet=Wallet.objects.get(name="Test wallet 1"),
        category=Category.objects.get(name="Food & Beverage"),
        date="2021-04-20",
        note="Dimsum",
    )

    Transaction.objects.create(
        name="Salary",
        amount=1500,
        wallet=Wallet.objects.get(name="Test wallet 1"),
        category=Category.objects.get(name="Salary"),
        date="2021-05-23",
        note="Duy's May salary - 1500$",
    )


@pytest.mark.django_db
class TestTransactiontAPI:
    def test_get_all_transactions(self, client, init_database):
        url = reverse("get-all-transactions")
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 3

    def test_get_transaction_by_id_on_empty_database_should_raise_DoesNotExist(
        self, client
    ):
        url = reverse("get-one-transaction", kwargs={"pk": 1})
        with pytest.raises(Transaction.DoesNotExist):
            response = client.get(url)
            assert response.status_code == 404

    def test_get_transaction_by_id_on_not_empty_database_should_pass(
        self, client, init_database
    ):
        tx = Transaction.objects.get(name="Salary")
        url = reverse("get-one-transaction", kwargs={"pk": tx.id})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["name"] == tx.name
        assert response.data["amount"] == str(tx.amount)
        assert response.data["wallet"] == tx.wallet.id
        assert response.data["category"] == tx.category.id

        tx_date = list(map(int, response.data["date"].split("-")))

        assert datetime.date(*tx_date) == tx.date
        assert response.data["note"] == tx.note
