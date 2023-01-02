from django.urls import path
from user_interface.views import register, login, dashboard, profile, change_password

urlpatterns = [
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("list-users/<int:page>", dashboard, name="list-users"),
    path("accounts/profile/", profile, name="profile"),
    path("change-password", change_password, name="change-password"),
]
