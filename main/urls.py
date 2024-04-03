from django.urls import path

from .views import get_main_page, get_basket_page, get_product_description_page, get_catalog_page, get_animal_products, \
    product_search_view

urlpatterns = [
    path('', get_main_page, name='main'),
    path('basket/', get_basket_page, name='basket'),
    path('catalog/', get_catalog_page, name='catalog'),
    path('search/', product_search_view, name='search'),
    path('animal_products/<int:id>/', get_animal_products, name='animal_products'),
    path('product_description/<int:id>/', get_product_description_page, name='product_description'),
]
