from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def get_cookie_page(request):
    response = render(request, 'cookie.html')
    response.set_cookie('color_back', request.COOKIES.get('color_js'))
    return response
