"""
This module consists of custom mixins
"""
from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AuthUserRestrictMixin:
    """This mixins restricts authenticated users to view pages like login, signup, forget password and so on"""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("location:index")
        return super().dispatch(request, *args, **kwargs)


class FormErrorMessageMixin:
    """This mixin displays the error messages"""

    error_message = None

    def form_invalid(self, form, *args, **kwargs):
        messages.add_message(self.request, messages.ERROR, self.error_message)
        return super().form_invalid(form, *args, **kwargs)


class CustomerRequiredMixin(AccessMixin):
    """
    Mixin to restrict access to views for customers only (users with is_customer=True).
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_customer:
            # Redirect to a login page or display a permission denied page as needed.
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
