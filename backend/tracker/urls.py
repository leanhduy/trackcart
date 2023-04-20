from django.urls import path
from tracker import views

urlpatterns = [
    path("currencies/", views.get_all_currencies, name="get-all-currencies"),
    path("currencies/<int:pk>", views.get_single_currency, name="get-one-currency"),
]
