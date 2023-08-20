from rest_framework.routers import DefaultRouter

from .views import FetchAllLocations

router = DefaultRouter()
router.register(r"delivery-locations", FetchAllLocations)

urlpatterns = router.urls
