from rest_framework.viewsets import ModelViewSet
from .models import Animal
from .serializers import AnimalSerializer


# Create your views here.

class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self):
        queryset = Animal.objects.all()
        order_by = self.request.query_params.get('orderBy')
        if order_by is None:
            order_by = 'name'
        return queryset.order_by(order_by)
