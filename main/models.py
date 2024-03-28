from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='animals/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_preview = models.ImageField(upload_to='products/')
    description = models.TextField()
    animal = models.ManyToManyField('Animal')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, blank=True, null=True)
    counter = models.PositiveIntegerField(default=0)    # счётчик покупок

    def __str__(self):
        return f'{self.counter} {self.name}'


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=50)
    percent = models.PositiveIntegerField()
    image = models.ImageField(upload_to='sales/')
    start = models.DateTimeField()
    finish = models.DateTimeField()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class ProductCount(models.Model):
    UNITS = {
        "шт": "шт",
        "л": "л",
        "кг": "кг",
    }
    value = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNITS)
    count = models.PositiveIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value} {self.product.name}'


class Article(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='articles/')
    description = models.TextField()
    time = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    author_name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=50)

    def __str__(self):
        return self.author_name
