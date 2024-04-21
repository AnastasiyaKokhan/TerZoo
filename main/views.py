from .models import Animal, Product, Brand, Review, Article, ProductCategory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import CartAddProductForm


# Create your views here.


def get_main_page(request):
    animals = Animal.objects.all()
    products = Product.objects.all().prefetch_related('productcount_set')
    popular_products = products.order_by('-counter')[:4]
    new_products = products.order_by('-id')[:4]
    brands = Brand.objects.all
    reviews = Review.objects.all()
    articles = Article.objects.all()
    cart_product_form = CartAddProductForm()

    context = {
        'animals': animals,
        'popular_products': popular_products,
        'new_products': new_products,
        'brands': brands,
        'reviews': reviews,
        'articles': articles,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'main.html', context)


def get_basket_page(request):
    popular_products = Product.objects.all().order_by('-counter')[:4]
    new_products = Product.objects.all().order_by('-id')[:4]
    articles = Article.objects.all()
    cart = Cart(request)

    context = {
        'popular_products': popular_products,
        'new_products': new_products,
        'articles': articles,
        'cart': cart,
    }

    return render(request, 'basket.html', context)


def get_catalog_page(request):
    animals = Animal.objects.all()
    categories = ProductCategory.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    popular_products = Product.objects.all().order_by('-counter')[:4]
    articles = Article.objects.all()
    date = request.POST.get('date')
    a_z = request.POST.get('a_z')
    z_a = request.POST.get('z_a')
    low_high = request.POST.get('low_high')
    high_low = request.POST.get('high_low')
    popular = request.POST.get('popular')

    if request.method == 'POST':
        get_category = request.POST.get('category')
        get_brands = request.POST.getlist('brand')
        if request.POST.get('promotional'):
            if request.POST.get('category'):
                products = products.filter(sale=True, category_id=get_category)
                if request.POST.get('brand'):
                    products = products.filter(brand_id__in=get_brands)
            elif request.POST.get('brand'):
                products = products.filter(sale=True, brand_id__in=get_brands)
            else:
                products = products.filter(sale=True)
        elif request.POST.get('category'):
            if request.POST.get('brand'):
                products = products.filter(category_id=get_category, brand_id__in=get_brands)
            else:
                products = products.filter(category_id=get_category)
        elif request.POST.get('brand'):
            products = products.filter(brand_id__in=get_brands)

    if request.method == 'POST':
        if request.POST.get('date'):
            products = products.order_by('-id')
        elif request.POST.get('low_high'):
            prices = []
            for product in products:
                if product.sale:
                    product_discounted_price = product.get_discounted_price()
                    prices.append(product_discounted_price)
                else:
                    product_price = product.price
                    prices.append(product_price)
            prices.sort()
            sorted_products = []
            for price in prices:
                for product in products:
                    if product.sale and product.get_discounted_price() == price:
                        sorted_products.append(product)
                    elif not product.sale and product.price == price:
                        sorted_products.append(product)
            products = sorted_products
        elif request.POST.get('high_low'):
            prices = []
            for product in products:
                if product.sale:
                    product_discounted_price = product.get_discounted_price()
                    prices.append(product_discounted_price)
                else:
                    product_price = product.price
                    prices.append(product_price)
            prices.sort(reverse=True)
            sorted_products = []
            for price in prices:
                for product in products:
                    if product.sale and product.get_discounted_price() == price:
                        sorted_products.append(product)
                    elif not product.sale and product.price == price:
                        sorted_products.append(product)
            products = sorted_products
        elif request.POST.get('a_z'):
            products = products.order_by('name')
        elif request.POST.get('z_a'):
            products = products.order_by('-name')
        elif request.POST.get('popular'):
            products = products.order_by('-counter')

    context = {
        'animals': animals,
        'categories': categories,
        'brands': brands,
        'products': products,
        'popular_products': popular_products,
        'articles': articles,
        'date': date,
        'a_z': a_z,
        'z_a': z_a,
        'low_high': low_high,
        'high_low': high_low,
        'popular': popular,
    }

    return render(request, 'catalog.html', context)


def product_search_view(request):
    animals = Animal.objects.all()
    categories = ProductCategory.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    popular_products = Product.objects.all().order_by('-counter')[:4]
    articles = Article.objects.all()
    search = request.POST.get('search')
    date = request.POST.get('date')
    a_z = request.POST.get('a_z')
    z_a = request.POST.get('z_a')
    low_high = request.POST.get('low_high')
    high_low = request.POST.get('high_low')
    popular = request.POST.get('popular')

    context = {
        'animals': animals,
        'categories': categories,
        'brands': brands,
        'products': products,
        'popular_products': popular_products,
        'articles': articles,
        'search': search,
        'date': date,
        'a_z': a_z,
        'z_a': z_a,
        'low_high': low_high,
        'high_low': high_low,
        'popular': popular,
    }

    if request.method == 'POST':
        if request.POST.get('search'):
            if len(request.POST.get('search')) >= 3:
                product_search = Product.objects.filter(name__icontains=search)
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
    date = request.POST.get('date')
    a_z = request.POST.get('a_z')
    z_a = request.POST.get('z_a')
    low_high = request.POST.get('low_high')
    high_low = request.POST.get('high_low')
    popular = request.POST.get('popular')

    if request.method == 'POST':
        get_category = request.POST.get('category')
        get_brands = request.POST.getlist('brand')
        if request.POST.get('promotional'):
            if request.POST.get('category'):
                products = products.filter(sale=True, category_id=get_category)
                if request.POST.get('brand'):
                    products = products.filter(brand_id__in=get_brands)
            elif request.POST.get('brand'):
                products = products.filter(sale=True, brand_id__in=get_brands)
            else:
                products = products.filter(sale=True)
        elif request.POST.get('category'):
            if request.POST.get('brand'):
                products = products.filter(category_id=get_category, brand_id__in=get_brands)
            else:
                products = products.filter(category_id=get_category)
        elif request.POST.get('brand'):
            products = products.filter(brand_id__in=get_brands)

    if request.method == 'POST':
        if request.POST.get('date'):
            products = products.order_by('-id')
        elif request.POST.get('low_high'):
            prices = []
            for product in products:
                if product.sale:
                    product_discounted_price = product.get_discounted_price()
                    prices.append(product_discounted_price)
                else:
                    product_price = product.price
                    prices.append(product_price)
            prices.sort()
            sorted_products = []
            for price in prices:
                for product in products:
                    if product.sale and product.get_discounted_price() == price:
                        sorted_products.append(product)
                    elif not product.sale and product.price == price:
                        sorted_products.append(product)
            products = sorted_products
        elif request.POST.get('high_low'):
            prices = []
            for product in products:
                if product.sale:
                    product_discounted_price = product.get_discounted_price()
                    prices.append(product_discounted_price)
                else:
                    product_price = product.price
                    prices.append(product_price)
            prices.sort(reverse=True)
            sorted_products = []
            for price in prices:
                for product in products:
                    if product.sale and product.get_discounted_price() == price:
                        sorted_products.append(product)
                    elif not product.sale and product.price == price:
                        sorted_products.append(product)
            products = sorted_products
        elif request.POST.get('a_z'):
            products = products.order_by('name')
        elif request.POST.get('z_a'):
            products = products.order_by('-name')
        elif request.POST.get('popular'):
            products = products.order_by('-counter')

    context = {
        'animals': animals,
        'categories': categories,
        'brands': brands,
        'products': products,
        'popular_products': popular_products,
        'articles': articles,
        'date': date,
        'a_z': a_z,
        'z_a': z_a,
        'low_high': low_high,
        'high_low': high_low,
        'popular': popular,
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


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('main')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('basket')


def add_animal(request):
    return render(request, 'add_animal.html')


def get_file(request):
    return render(request, 'file2.html')
