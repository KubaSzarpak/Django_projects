from django.db import models


# Create your models here.

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    amount = models.IntegerField()
    created_at = models.DateTimeField()
    fulfilled_at = models.DateTimeField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.pk


class ProductWarehouse(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='product_warehouses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_warehouses')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_warehouses')
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField()
    objects = models.Manager()
