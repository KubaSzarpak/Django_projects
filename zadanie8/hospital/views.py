from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Doctor, Prescription
from .serializers import DoctorSerializer, PrescriptionSerializer


# Create your views here.

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]


class PrescriptionViewSet(ListModelMixin,
                          GenericViewSet):
    queryset = Prescription.objects.select_related('patient', 'doctor').prefetch_related('medicaments__medicament')
    serializer_class = PrescriptionSerializer
