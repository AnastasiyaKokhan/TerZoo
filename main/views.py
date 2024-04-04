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
    filtered_products = None
    sorted_products = None

    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('promotional'):
            category = request.POST.get('category')
            brands1 = request.POST.getlist('brand')
            if request.POST.get('category'):
                filtered_products = products.filter(sale=True, category_id=category)
                print(filtered_products)
                if request.POST.get('brand'):
                    filtered_products = filtered_products.filter(brand_id__in=brands1)
            elif request.POST.get('brand'):
                filtered_products = products.filter(sale=True, brand_id__in=brands1)
            else:
                filtered_products = products.filter(sale=True)
            print(filtered_products)
        elif request.POST.get('category'):
            category = request.POST.get('category')
            brands1 = request.POST.getlist('brand')
            if request.POST.get('brand'):
                filtered_products = products.filter(category_id=category, brand_id__in=brands1)
            else:
                filtered_products = products.filter(category_id=category)
        elif request.POST.get('brand'):
            brands1 = request.POST.getlist('brand')
            filtered_products = products.filter(brand_id__in=brands1)
    print(filtered_products)

    if request.method == 'POST':
        if request.POST.get('date'):
            sorted_products = products.order_by('-id')
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
        elif request.POST.get('a_z'):
            sorted_products = products.order_by('name')
        elif request.POST.get('z_a'):
            sorted_products = products.order_by('-name')
        elif request.POST.get('popular'):
            sorted_products = products.order_by('-counter')
    print(filtered_products)
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
        'filtered_products': filtered_products,
        'sorted_products': sorted_products,
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
                # if request.POST.get('date'):
                #     product_search = product_search.order_by('-id')
                #     print(product_search)

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
    filtered_products = None
    sorted_products = None

    if request.method == 'POST':
        if request.POST.get('promotional'):
            category = request.POST.get('category')
            brands = request.POST.getlist('brand')
            if request.POST.get('category'):
                filtered_products = products.filter(sale=True, category_id=category)
                if request.POST.get('brand'):
                    filtered_products = filtered_products.filter(brand_id__in=brands)
            elif request.POST.get('brand'):
                filtered_products = products.filter(sale=True, brand_id__in=brands)
            else:
                filtered_products = products.filter(sale=True)
        elif request.POST.get('category'):
            category = request.POST.get('category')
            brands = request.POST.getlist('brand')
            if request.POST.get('brand'):
                filtered_products = products.filter(category_id=category, brand_id__in=brands)
            else:
                filtered_products = products.filter(category_id=category)
        elif request.POST.get('brand'):
            brands = request.POST.getlist('brand')
            filtered_products = products.filter(brand_id__in=brands)

    if request.method == 'POST':
        if request.POST.get('date'):
            sorted_products = products.order_by('-id')
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
        elif request.POST.get('a_z'):
            sorted_products = products.order_by('name')
        elif request.POST.get('z_a'):
            sorted_products = products.order_by('-name')
        elif request.POST.get('popular'):
            sorted_products = products.order_by('-counter')

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
        'filtered_products': filtered_products,
        'sorted_products': sorted_products,
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

