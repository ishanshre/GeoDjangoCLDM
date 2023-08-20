from django.urls import path

from . import views

app_name = "location"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create/", views.LocationCreateView.as_view(), name="location_create"),
    path(
        "<slug:slug>/detail/",
        views.LocationDetailView.as_view(),
        name="location_detail",
    ),
    path(
        "<slug:slug>/delete/",
        views.LocationDeleteView.as_view(),
        name="location_delete",
    ),
    path(
        "<slug:slug>/update/",
        views.LocationUpdateView.as_view(),
        name="location_update",
    ),
]
