"""
This module contains forms related to User creation, change and authentication
"""

from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    A custom form for user registration (creation).

    This form inherits from Django's built-in UserCreationForm and customizes it
    for our User model.

    Fields:
    - username: The desired username for the user.
    - email: The user's email address.
    - full_name: The user's full name.
    - date_of_birth: The user's date of birth.
    """

    class Meta(UserCreationForm.Meta):
        """
        It contains the meta data for user creaton form
        """

        model = User
        fields = ["username", "email", "full_name", "is_customer", "is_employee"]


class CustomUserChangeForm(UserChangeForm):
    """
    A custom form for user profile editing (change).

    This form inherits from Django's built-in UserChangeForm and customizes it
    for our User model.

    Fields:
    - username: The user's username.
    - email: The user's email address.
    - full_name: The user's full name.
    - is_customer: Customer boolean
    """

    class Meta:
        """
        It contains the meta data for user change form
        """

        model = User
        fields = ["username", "email", "full_name", "is_customer", "is_employee"]


class UserLoginForm(AuthenticationForm):
    """
    LoginForm that inherits builtin AuthenticationForm
    """

    class Meta:
        model = User
        fields = ["username", "password"]


class CustomerSignUp(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = User
        fields = ["username", "email", "full_name"]

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user
