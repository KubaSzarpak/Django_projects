from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('trips', views.TripsViewSet, basename='trips')
router.register('clients', views.ClientViewSet, basename='clients')

trip_nested_router = routers.NestedDefaultRouter(router, 'trips', lookup='trip')
trip_nested_router.register('clients', views.ClientTripViewSet, basename='trip_clients')

urlpatterns = router.urls + trip_nested_router.urls
