from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models import Customer


class DeliveryLocation(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="delivery_locations"
    )
    name = models.CharField(max_length=255, help_text="A name for delivery location")
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    location = models.PointField(
        geography=True, help_text="The geographic location of the delivery address"
    )
    is_primary = models.BooleanField(
        default=False, help_text="Is this location primary"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            username = self.customer.user.username
            combined = f"{username}-{self.name}"
            self.slug = slugify(combined)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("location:location_detail", args=[self.slug])
