from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="account:login"), name="logout"),
]
