from django.urls import path
from user_auth.views import logout_user

urlpatterns = [
    path("logout", logout_user, name="logout"),
]
