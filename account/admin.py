"""
This miodule customizes models the admin pannel
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from leaflet.admin import LeafletGeoAdminMixin

from account.forms import CustomUserChangeForm, CustomUserCreationForm
from account.models import Customer, Employee, Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    """
    Display Profile model as inline with user
    """

    model = Profile


class EmployeeInline(LeafletGeoAdminMixin, admin.StackedInline):
    """
    Display Employee model as inline with user
    """

    model = Employee


class CustomerInline(admin.StackedInline):
    """
    Display Customer model as inline with user
    """

    model = Customer


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Customizes the User model for the Django admin panel.

    This class extends Django's built-in UserAdmin and adds
    customizations specific to our User model.

    Attributes:
    - list_display: The fields to display in the user list in the admin panel.
    - add_form: The form to use for adding new users.
    - form: The form to use for editing user profiles.
    - fieldsets: Defines the layout of fields in the user edit page.
    - add_fieldsets: Defines the layout of fields
    in the user registration page.

    Note: The User model is registered with the admin panel using
    the @admin.register
    decorator.
    """

    list_display = ["username", "is_employee", "is_customer"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
        (
            (
                "Change Detail",
                {
                    "fields": ("full_name", "is_employee", "is_customer"),
                },
            )
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            (
                "User Registration",
                {
                    "classes": ("wide",),
                    "fields": (
                        "username",
                        "email",
                        "full_name",
                        "is_employee",
                        "is_customer",
                        "password1",
                        "password2",
                    ),
                },
            )
        ),
    )

    def get_inlines(self, request, obj=None):
        if obj:
            if obj.is_employee:
                return [ProfileInline, EmployeeInline]
            if obj.is_customer:
                return [ProfileInline, CustomerInline]
            return [ProfileInline]
        return []
