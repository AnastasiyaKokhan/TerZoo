from decimal import Decimal

from django.shortcuts import render

from .models import Animal, Product, Brand, Review, Article


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
    return render(request, 'basket.html')


def get_product_description_page(request, id):
    product = Product.objects.get(id=id)

    price = {}
    for value in product.productcount_set.all():
        price[value] = float(product.price) * value.value
        print(price)

    popular_products = Product.objects.all().order_by('-counter')[:4]
    similar_products = Product.objects.all().order_by('counter')[:4]
    articles = Article.objects.all()

    context = {
        'product': product,
        'price': price,
        'popular_products': popular_products,
        'similar_products': similar_products,
        'articles': articles,
    }
    return render(request, 'product_description.html', context)


def get_test_page(request):
    animals = Animal.objects.all()

    context = {
        'animals': animals,
    }

    if request.method == 'POST':
        if request.POST.get('search'):
            if len(request.POST.get('search')) >= 2:
                product_search = Product.objects.filter(name__lte=request.POST.get('search'))
                context['product_search'] = product_search
            else:
                context['error'] = 'поиск от 3 букв'

    return render(request, 'test.html', context)
