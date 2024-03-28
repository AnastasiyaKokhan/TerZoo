from django.contrib import admin

from .models import Animal, Product, Brand, Sale, ProductCategory, ProductImage, ProductCount, Review, Article

# Register your models here.

admin.site.register(Animal)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Sale)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(ProductCount)
admin.site.register(Article)
admin.site.register(Review)
