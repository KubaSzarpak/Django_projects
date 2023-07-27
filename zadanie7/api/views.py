from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from .models import Trip, Client, ClientTrip
from .serializers import TripSerializer, SimpleClientSerializer, AddClientTripSerializer


# Create your views here.

class TripsViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    queryset = Trip.objects.prefetch_related('clients__client', 'countries__country').all()
    serializer_class = TripSerializer


class ClientViewSet(DestroyModelMixin,
                    GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = SimpleClientSerializer


class ClientTripViewSet(CreateModelMixin,
                        GenericViewSet):
    queryset = ClientTrip.objects.all()
    serializer_class = AddClientTripSerializer
