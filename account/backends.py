from typing import Any, Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

User = get_user_model()


class CustomAuthBackend(ModelBackend):
    def authenticate(
        self,
        request: HttpRequest,
        username: str | None = ...,
        password: str | None = ...,
        **kwargs: Any
    ) -> AbstractBaseUser | None:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.is_superuser or user.is_customer:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
