from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import DeliveryLocation


class CreateDeliveryLocationForm(forms.ModelForm):
    class Meta:
        model = DeliveryLocation
        fields = ["name", "location", "is_primary"]
        widgets = {"location": LeafletWidget()}
        labels = {"is_primary": "Set As Default Delivery Location"}
