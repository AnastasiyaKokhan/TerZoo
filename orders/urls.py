from django.urls import path
from .views import order_create

urlpatterns = [
    path('order/', order_create, name='order_create'),
]
