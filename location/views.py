from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from account.mixins import FormErrorMessageMixin

from .forms import CreateDeliveryLocationForm
from .models import DeliveryLocation

# Create your views here.


class IndexView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of delivery locations for the logged-in user's customer.

    Attributes:
        model (class): The model to use for retrieving delivery locations.
        template_name (str): The HTML template for rendering the view.
        context_object_name (str): The variable name used in the template to access the list of
        delivery locations.
        paginate_by (int): Number of locations to display per page in pagination.

    Methods:
        get_queryset(self) -> QuerySet[Any]: Retrieves the queryset of delivery locations.
    """

    model = DeliveryLocation
    template_name = "index.html"
    context_object_name = "locations"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        # return self.model.objects.filter(customer=self.request.user.customer)
        # optimized query set. Filter delivery location by the user associated with
        # the logged-in user
        return (
            self.request.user.customer.delivery_locations.all()
            .select_related("customer__user")
            .order_by("-is_primary")
        )


class LocationDetailView(LoginRequiredMixin, DetailView):
    """
    Get the queryset of delivery locations for the logged-in user's customer.

    Returns:
        QuerySet[Any]: The queryset of delivery locations.
    """

    model = DeliveryLocation
    template_name = "location/location_detail.html"
    context_object_name = "location"


class LocationCreateView(
    LoginRequiredMixin, SuccessMessageMixin, FormErrorMessageMixin, CreateView
):
    """
    View for creating a new delivery location.

    Attributes:
        form_class (class): The form class for creating a delivery location.
        template_name (str): The HTML template for rendering the view.
        success_url (str): The URL to redirect to upon successful creation.
        success_message (str): The success message to display.
        error_message (str): The error message to display.

    Methods:
        form_valid(self, form): Handles form validation and sets the customer for the new location.
    """

    form_class = CreateDeliveryLocationForm
    template_name = "location/location_create.html"
    success_url = reverse_lazy("location:index")
    success_message = "Location Created Sucessfully"
    error_message = "Location Not Created"

    def form_valid(self, form):
        """
        Handle customer field after form is valid
        """
        form.instance.customer = self.request.user.customer
        if form.cleaned_data["is_primary"]:
            with transaction.atomic():
                self.request.user.customer.delivery_locations.update(is_primary=False)
        return super(LocationCreateView, self).form_valid(form)


class LocationDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    FormErrorMessageMixin,
    DeleteView,
):
    """
    View for deleting a delivery location.

    Attributes:
        model (class): The model to use for deleting a delivery location.
        template_name (str): The HTML template for rendering the view.
        success_url (str): The URL to redirect to upon successful deletion.
        success_message (str): The success message to display.
        error_message (str): The error message to display.

    Methods:
        test_func(self) -> bool | None: Tests if the user has permission to delete the location.
    """

    model = DeliveryLocation
    template_name = "location/location_delete.html"
    success_url = reverse_lazy("location:index")
    success_message = "Location Deleted"
    error_message = "Error in deleting location"

    def test_func(self) -> bool | None:
        """
        Check if owner of location matches with the customer associated with logged user
        """
        self.obj = self.get_object()
        return self.obj.customer == self.request.user.customer


class LocationUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    FormErrorMessageMixin,
    UpdateView,
):
    """
    View for updating a delivery location.

    Attributes:
        model (class): The model to use for updating a delivery location.
        form_class (class): The form class for updating a delivery location.
        template_name (str): The HTML template for rendering the view.
        success_message (str): The success message to display on success
        error_message (str): The error message to display on error
    """

    model = DeliveryLocation
    form_class = CreateDeliveryLocationForm
    template_name = "location/location_update.html"
    success_message = "Location Updated"
    error_message = "Error in updating location"

    def form_valid(self, form: BaseForm) -> HttpResponse:
        if form.cleaned_data["is_primary"]:
            with transaction.atomic():
                self.request.user.customer.delivery_locations.exclude(
                    pk=self.get_object().pk
                ).update(is_primary=False)

    def test_func(self) -> bool | None:
        self.obj = self.get_object()
        return self.obj.customer == self.request.user.customer
