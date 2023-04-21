from django.urls import path
from tracker import views

urlpatterns = [
    path("currencies/", views.get_all_currencies, name="get-all-currencies"),
    path("currencies/<int:pk>", views.get_single_currency, name="get-one-currency"),
    path("categories", views.get_all_categories, name="get-all-categories"),
    path("categories/<int:pk>", views.get_single_category, name="get-one-category"),
    # path("wallets", views.get_all_wallets, name="get-all-wallets"),
    # path("wallets/<int:pk>", views.get_single_wallet, name="get-one-wallet"),
]
