from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)  # Kitob zaxirasi

    def __str__(self):
        return self.title

