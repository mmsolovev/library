from django.test import TestCase

from orders.models import SalesOrder
from orders.serializers import OrderSerializer


class OrderSerializerTestCase(TestCase):
    def test_ok(self):
        order_1 = SalesOrder.objects.create(amount=2, description='Text')
        order_2 = SalesOrder.objects.create(amount=1, description='Another text')
        data = OrderSerializer([order_1, order_2], many=True).data
        expected_data = [
            {
                'id': order_1.id,
                'amount': 2,
                'description': 'Text',
            },
            {
                'id': order_2.id,
                'amount': 1,
                'description': 'Another text',
            },
        ]
        self.assertEqual(expected_data, data)
