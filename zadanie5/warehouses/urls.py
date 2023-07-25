from warehouses import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('warehouses', views.ProductWarehouseViewSet)

urlpatterns = router.urls
