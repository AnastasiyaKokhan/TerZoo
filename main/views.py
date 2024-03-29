from decimal import Decimal

from django.shortcuts import render, redirect

from .models import Animal, Product, Brand, Review, Article, ProductCategory


# Create your views here.


def get_main_page(request):
    animals = Animal.objects.all()
    products = Product.objects.all().prefetch_related('productcount_set')
    popular_products = products.order_by('-counter')[:4]
    new_products = products.order_by('-id')[:4]
    brands = Brand.objects.all
    reviews = Review.objects.all()
    articles = Article.objects.all()

    context = {
        'animals': animals,
        'popular_products': popular_products,
        'new_products': new_products,
        'brands': brands,
        'reviews': reviews,
        'articles': articles,
    }

    return render(request, 'main.html', context)


def get_basket_page(request):
    popular_products = Product.objects.all().order_by('-counter')[:4]
    new_products = Product.objects.all().order_by('-id')[:4]
    articles = Article.objects.all()

    context = {
        'popular_products': popular_products,
        'new_products': new_products,
        'articles': articles,
    }

    return render(request, 'basket.html', context)


def get_catalog_page(request):
    animals = Animal.objects.all()
    categories = ProductCategory.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    popular_products = Product.objects.all().order_by('-counter')[:4]
    articles = Article.objects.all()

    context = {
        'animals': animals,
        'categories': categories,
        'brands': brands,
        'products': products,
        'popular_products': popular_products,
        'articles': articles,
    }

    if request.method == 'POST':
        if request.POST.get('search'):
            if len(request.POST.get('search')) >= 3:
                product_search = Product.objects.filter(name__icontains=request.POST.get('search'))
                context['product_search'] = product_search

    return render(request, 'catalog.html', context)


def get_animal_products(request, id):
    animal = Animal.objects.get(id=id)
    products = Product.objects.filter(animal=animal)
    animals = Animal.objects.all()
    categories = ProductCategory.objects.all()
    brands = Brand.objects.all()
    popular_products = Product.objects.all().order_by('-counter')[:4]
    articles = Article.objects.all()

    context = {
        'animal': animal,
        'products': products,
        'animals': animals,
        'categories': categories,
        'brands': brands,
        'popular_products': popular_products,
        'articles': articles,
    }

    return render(request, 'catalog.html', context)


def get_product_description_page(request, id):
    product = Product.objects.get(id=id)
    popular_products = Product.objects.all().order_by('-counter')[:4]
    similar_products = Product.objects.all().order_by('counter')[:4]
    articles = Article.objects.all()

    price = {}
    for value in product.productcount_set.all():
        price[value] = float(product.price) * value.value
        print(price)

    context = {
        'product': product,
        'price': price,
        'popular_products': popular_products,
        'similar_products': similar_products,
        'articles': articles,
    }

    return render(request, 'product_description.html', context)
