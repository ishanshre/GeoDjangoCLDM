from typing import Iterable, Optional

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import GEOSGeometry
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email: models.EmailField = models.EmailField(
        max_length=255, unique=True, db_index=True
    )
    username: models.CharField = models.CharField(
        max_length=255, unique=True, db_index=True
    )
    full_name: models.CharField = models.CharField(max_length=255)
    is_active: models.BooleanField = models.BooleanField(default=True)
    is_staff: models.BooleanField = models.BooleanField(default=False)
    is_employee: models.BooleanField = models.BooleanField(default=False)
    is_customer: models.BooleanField = models.BooleanField(default=False)
    joined_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    objects: CustomUserManager = CustomUserManager()

    # Define the field to use as the username for authentication
    USERNAME_FIELD: str = "username"

    # Define the required fields to use as the username when authenticating
    REQUIRED_FIELDS: list = ["email", "full_name", "is_customer", "is_employee"]

    def __str__(self) -> str:
        """
        Return the username as a string representation of the user.

        Returns:
            str: The username of the user.
        """
        return f"{self.username}"


class Profile(models.Model):
    user: models.OneToOneField = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    date_of_birth: models.DateField = models.DateField(
        db_index=True, null=True, blank=True
    )
    phone_number: PhoneNumberField = PhoneNumberField(
        region="NP", null=True, blank=True
    )
    avatar: models.ImageField = models.ImageField(
        upload_to="user/images", null=True, blank=True
    )
    bio: models.TextField = models.TextField(max_length=10000)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")

    def __str__(self):
        return self.user.username


class Employee(geomodels.Model):
    lat = geomodels.FloatField(null=True, blank=True)
    lon = geomodels.FloatField(null=True, blank=True)
    point = geomodels.PointField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")

    def save(self, *args, **kwargs):
        if self.point:
            point = GEOSGeometry(self.point)
            self.lat = point.y
            self.lon = point.x
        super().save(*args, **kwargs)
