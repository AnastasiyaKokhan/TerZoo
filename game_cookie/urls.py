from django.urls import path

from .views import get_cookie_page

urlpatterns = [
    path('', get_cookie_page),
]