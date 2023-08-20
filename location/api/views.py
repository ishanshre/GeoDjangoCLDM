from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from location.models import DeliveryLocation

from .serializers import DeliveryLocationSerializer


class FetchAllLocations(viewsets.ReadOnlyModelViewSet):
    """
    A read-only viewset for fetching all delivery locations.

    This viewset provides read-only access to all `DeliveryLocation` instances, allowing
    users to retrieve a list of all delivery locations stored in the database.

    Attributes:
        serializer_class: The serializer used to convert `DeliveryLocation` instances
                          into JSON format for API responses.
        queryset: The database query that retrieves all `DeliveryLocation` instances.

    """

    serializer_class = DeliveryLocationSerializer
    queryset = DeliveryLocation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_primary"]
