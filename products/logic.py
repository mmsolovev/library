from django.db.models import Avg

from products.models import UserBookRelation


def set_rating(book):
    rating = UserBookRelation.objects.filter(book=book).aggregate(reting=Avg('rate')).get('rating')
    book.rating = rating
    book.save()
