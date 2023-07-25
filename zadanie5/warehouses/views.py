from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import ProductWarehouse
from .serializers import ProductWarehouseSerializer


# Create your views here.

class ProductWarehouseViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = ProductWarehouse.objects.all()
    serializer_class = ProductWarehouseSerializer

    def get_serializer_context(self):
        return {'product_id': self.request.POST.get('product'),
                'amount': self.request.POST.get('amount'),
                'created_at': self.request.POST.get('created_at')}




