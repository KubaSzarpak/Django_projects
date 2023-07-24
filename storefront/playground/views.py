from django.shortcuts import render
from django.db.models import Q, F, Count
from store.models import Product, Customer, Order, OrderItem


# Create your views here.

def say_hello(request):
    # query_set = Product.objects.filter(collection__id__range=(1, 4))
    # query_set = Product.objects.filter(title__icontains='coffee')
    # query_set = Product.objects.filter(last_update__year=2021)
    # query_set = Product.objects.filter(description__isnull=True)

    # exercises
    # query_set = Customer.objects.filter(email__endswith='.com')
    # query_set = Product.objects.filter(inventory__lt=10)
    # query_set = Order.objects.filter(customer__id=1)
    # query_set = OrderItem.objects.filter(product__collection__id=3)

    # Products: inventory<10 AND price<20
    # query_set = Product.objects.filter(inventory__lt=10, price__lt=20)
    # query_set = Product.objects.filter(inventory__lt=10).filter(price__lt=20)

    # Products: inventory<10 OR NOT price<20
    # query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(price__lt=20))

    # Products: inventory=price
    # query_set = Product.objects.filter(inventory=F('price'))

    # query_set = Product.objects.order_by('price', '-title').reverse()

    # ordered_items_indexes = OrderItem.objects.values('product_id')
    # query_set = Product.objects.filter(id__in=ordered_items_indexes).order_by('title')

    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]
    first = Product.objects.filter(pk=0).first()

    customers = Customer.objects.annotate(orders_count=Count('order'))
    list(customers)

    return render(request, 'hello.html',
                  {'name': 'Jakub', 'length': len(query_set), 'products': list(query_set), 'first': first})
