import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Book, UserBookRelation


class BookRelationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username',)
        self.user_2 = User.objects.create(username='test_username2',)
        self.book = Book.objects.create(name='Test book 1',
                                        price=300,
                                        author='Test author 1',
                                        owner=self.user)
        self.book_2 = Book.objects.create(name='Test book 2',
                                          price=1000,
                                          author='Test author 2')

    def test_like(self):
        url = reverse('userbookrelation-detail', args=(self.book.id,))

        data = {
            "Like": True,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user,
                                                book=self.book)
        self.assertTrue(relation.like)
        relation_2 = UserBookRelation.objects.get(user_2=self.user,
                                                  book_2=self.book)
        self.assertTrue(relation_2.like)
