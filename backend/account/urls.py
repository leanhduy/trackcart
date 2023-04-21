from django.urls import path
from account import views

urlpatterns = [
    path("profiles/", views.get_all_profiles, name="get-all-profiles"),
    path("profiles/<uuid:pk>", views.get_single_profile , name="get-one-profile"),
    path("users/", views.get_all_users, name="get-all-users"),
    path("users/<int:pk>", views.get_single_user , name="get-one-user"),
]
