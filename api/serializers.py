from rest_framework import serializers

from .models import Author, Book, Shop
from main.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image_preview = serializers.ImageField()


class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    shop_set = ShopSerializer(many=True)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    book_set = BookSerializer(many=True)


class AuthorSerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class BookSerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    author = AuthorSerializer1(many=True)


class ShopSerializer1(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    book = BookSerializer1()

