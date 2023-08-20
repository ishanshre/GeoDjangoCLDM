from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomerSignUp, UserLoginForm
from .mixins import AuthUserRestrictMixin, FormErrorMessageMixin


class SignUpView(
    AuthUserRestrictMixin, SuccessMessageMixin, FormErrorMessageMixin, CreateView
):
    form_class = CustomerSignUp
    template_name = "account/signup.html"
    success_message = "User Sign Up Successful"
    error_message = "User Registration Error"

    def get_success_url(self) -> str:
        return reverse_lazy("account:login")


class UserLoginView(
    AuthUserRestrictMixin, SuccessMessageMixin, FormErrorMessageMixin, LoginView
):
    form_class = UserLoginForm
    template_name = "account/login.html"
    success_message = "Login Success"
    error_message = "User login errror"
