from django.contrib.auth.models import User
from django.test import TestCase

from products.logic import set_rating
from products.models import Book, UserBookRelation


class LogicTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create(username='user1', first_name='Ivan', last_name='Ivanov')
        user_2 = User.objects.create(username='user2', first_name='Petr', last_name='Petrov')
        user_3 = User.objects.create(username='user3', first_name='Maksim', last_name='Maksimov')

        self.book_1 = Book.objects.create(name='testbook1', author='author1', price=300, owner=user_1)

        UserBookRelation.objects.create(user=user_1, book=self.book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=user_2, book=self.book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=user_3, book=self.book_1, like=True, rate=4)

    def test_ok(self):
        set_rating(self.book_1)
        self.book_1.refresh_from_db
        self.assertEqual('4.67', str(self.book_1.rating))
