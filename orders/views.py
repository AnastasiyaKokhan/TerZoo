from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                new_order_item = OrderItem(order=order,
                                           product=item['product'],
                                           price=float(item['price']),
                                           quantity=item['quantity'])
                new_order_item.save()
            # cart.clear()
            return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'cart': cart, 'form': form})
