from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Author, Book, Shop
from .serializers import AnimalSerializer, ProductSerializer, AuthorSerializer, ShopSerializer1
from main.models import Animal, Product


# Create your views here.

# @api_view(['GET', 'POST'])
# def get_animal_list(request):
#     animals = Animal.objects.all()
#     serializer = AnimalSerializer(animals, many=True)
#     return Response(serializer.data)


class AnimalListAPIView(ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


@api_view(['GET'])
def search_products(request):
    products = Product.objects.filter(name__icontains=request.query_params.get('search'))
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)


@api_view(['POST'])
def add_animal(request):
    new_animal = AnimalSerializer(data=request.data)
    if new_animal.is_valid(raise_exception=True):
        new_animal = Animal(name=new_animal.validated_data.get('name'), image=new_animal.validated_data.get('image'))
        new_animal.save()
    return Response()


@api_view(['GET'])
def author_books(request):
    authors = Author.objects.all()
    serialized_authors = AuthorSerializer(authors, many=True)
    return Response(serialized_authors.data)


@api_view(['GET'])
def shop_books(request):
    shops = Shop.objects.all()
    serialized_shops = ShopSerializer1(shops, many=True)
    return Response(serialized_shops.data)
