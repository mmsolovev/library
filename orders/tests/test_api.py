from django.urls import reverse
from rest_framework.test import APITestCase


class OrderApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('orders-list')
        print(url)
        response = self.client.get(url)
        print(response)
