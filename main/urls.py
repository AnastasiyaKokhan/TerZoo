from django.urls import path

from .views import get_main_page, get_test_page, get_product_description_page, get_basket_page

urlpatterns = [
    path('', get_main_page, name='main'),
    path('basket/', get_basket_page, name='basket'),
    path('product_description/<int:id>/', get_product_description_page, name='product_description'),
    path('test/', get_test_page, name='test'),
]
