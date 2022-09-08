from django.db.models import Count, Case, When, Avg
from django.test import TestCase

from products.models import Book
from products.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(price=300, name='Bookname 1', author='Author 1')
        book_2 = Book.objects.create(price=200, name='Bookname 2', author='Author 2')
        books = Book.objects.all().annotate(
            annotted_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')
        ).order_by('id')
        data = BookSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'price': 300,
                'name': 'Bookname 1',
                'author': 'Author 1',
                'likes_count': 0,
                'annotated_likes': 3,
                'rating': 0
            },
            {
                'id': book_2.id,
                'price': 200,
                'name': 'Bookname 2',
                'author': 'Author 2',
                'likes_count': 0,
                'annotated_likes': 3,
                'rating': 0
            },
        ]
        self.assertEqual(expected_data, data)
