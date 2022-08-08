from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


class OrderApiTestCase(APITestCase):
    def test_get(self):
        order_1 = SalesOrder.objects.create(amount=2, description='Text')
        order_2 = SalesOrder.objects.create(amount=1, description='Another text')
        url = reverse('orders-list')
        response = self.client.get(url)
        serializer_data = OrderSerializer([order_1, order_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

