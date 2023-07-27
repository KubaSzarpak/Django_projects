from rest_framework.routers import DefaultRouter

from hospital import views

router = DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('prescriptions', views.PrescriptionViewSet)

urlpatterns = router.urls
