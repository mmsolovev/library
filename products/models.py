from django.db import models


class Book(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} : {self.name}'

