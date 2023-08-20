from django.contrib.gis.db import models

from account.models import Customer


class DeliveryLocation(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="delivery_locations"
    )
    name = models.CharField(max_length=255, help_text="A name for delivery location")
    location = models.PointField(
        geography=True, help_text="The geographic location of the delivery address"
    )
    is_primary = models.BooleanField(
        default=False, help_text="Is this location primary"
    )

    def __str__(self):
        return self.name
