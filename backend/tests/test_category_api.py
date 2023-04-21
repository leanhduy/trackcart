"""
This file contains the test class to test the Category API.
"""
import pytest
from django.urls import reverse
from tracker.models import Category


# Fixtures
@pytest.fixture
def init_database():
    """This fixture is used to initialize the database with some data.
    """
    Category.objects.create(
        name="Food & Beverage", cate_type="expense", sub_category="required"
    )
    Category.objects.create(name="Salary", cate_type="income", sub_category="income")
    Category.objects.create(name="Pets", cate_type="expense", sub_category="other")


@pytest.mark.django_db
class TestCategoryAPI:
    def test_get_all_categories(self, client, init_database):
        url = reverse("get-all-categories")
        response = client.get(url)
        assert response.status_code == 200

    def test_get_category_by_id_on_empty_database_should_raise_DoesNotExist(
        self, client
    ):
        url = reverse("get-one-category", kwargs={'pk': 1})
        with pytest.raises(Category.DoesNotExist):
            response = client.get(url)
            assert response.status_code == 404

    def test_get_category_by_id_on_not_empty_database_should_pass(self, client, init_database):
        id = Category.objects.get(name="Food & Beverage").id
        url = reverse("get-one-category", kwargs={'pk': 1})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data['name'] == 'Food & Beverage'