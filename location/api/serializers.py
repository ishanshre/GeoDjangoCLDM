from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from location.models import DeliveryLocation


class DeliveryLocationSerializer(GeoFeatureModelSerializer):
    """
    Serializer for the `DeliveryLocation` model that extends `GeoFeatureModelSerializer`.

    This serializer is used to convert `DeliveryLocation` model instances into GeoJSON format
    suitable for API responses. It inherits from `GeoFeatureModelSerializer` to include
    geographic data for the 'location' field.

    Attributes:
        Meta: A nested class that specifies metadata for the serializer, including the
              model it's based on, the fields to include, and the geo_field for geographic data.
    """

    customer_name = serializers.SerializerMethodField()
    location_name = serializers.CharField(
        source="name"
    )  # change the key from name to location_name

    class Meta:
        model = DeliveryLocation
        fields = [
            "id",
            "location_name",
            "location",
            "is_primary",
            "customer_name",
        ]
        geo_field = "location"

    def get_customer_name(self, obj):
        user = obj.customer.user if obj.customer else None
        if user:
            return f"{user.full_name}"
        return None
