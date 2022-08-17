from django.test import TestCase

from products.models import Book
from products.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(price=300, name='Bookname 1', author='Author 1')
        book_2 = Book.objects.create(price=200, name='Bookname 2', author='Author 2')
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'price': 300,
                'name': 'Bookname 1',
                'author': 'Author 1',
            },
            {
                'id': book_2.id,
                'price': 200,
                'name': 'Bookname 2',
                'author': 'Author 2',
            },
        ]
        self.assertEqual(expected_data, data)
