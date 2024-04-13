from django.urls import path
from .views import search_products, AnimalListAPIView, add_animal, author_books, shop_books

urlpatterns = [
    # path('get_animal_list/', get_animal_list),
    path('get_animal_list/', AnimalListAPIView.as_view()),
    path('search_products/', search_products),
    path('add_animal/', add_animal),
    path('author_books/', author_books),
    path('shop_books/', shop_books),
]