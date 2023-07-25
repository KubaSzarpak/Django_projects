from MySQLdb.times import DateTimeType
from _decimal import Decimal
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import ProductWarehouse, Order, Product


class ProductWarehouseSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)

    class Meta:
        model = ProductWarehouse
        fields = ['warehouse', 'product', 'order', 'amount', 'price', 'created_at']

    def create(self, validated_data):
        product_id = self.context['product_id']
        amount = self.context['amount']
        created_at = self.context['created_at']

        order_id_queryset = Order.objects.filter(product_id=product_id, amount=amount, created_at__lt=created_at).values('id').first()

        if order_id_queryset is None:
            raise serializers.ValidationError('There is not such order')

        order_id = order_id_queryset['id']
        exists = ProductWarehouse.objects.filter(order_id=order_id).exists()

        if exists:
            raise serializers.ValidationError('This order is already completed')

        product_price = Product.objects.filter(pk=product_id).values('price').get()['price']
        price = product_price * Decimal(amount)
        Order.objects.filter(id=order_id).update(fulfilled_at=DateTimeType.now())
        return ProductWarehouse.objects.create(order_id=order_id, price=price, **validated_data)
