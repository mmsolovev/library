from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['amount']


def orders_app(request):
    return render(request, 'main_app.html')
