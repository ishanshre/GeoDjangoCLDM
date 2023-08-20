from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import DeliveryLocation

# Register your models here.

admin.site.register(DeliveryLocation, LeafletGeoAdmin)
