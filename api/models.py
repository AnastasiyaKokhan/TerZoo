from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey('Book', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
