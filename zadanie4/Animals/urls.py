from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('animals', views.AnimalViewSet)

urlpatterns = router.urls
