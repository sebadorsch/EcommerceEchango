from django.conf.urls import url
from django.http import JsonResponse
from api.views import api_home, get_user, register_user, get_producto, get_productos

urlpatterns = [
    url(r'^$', api_home, name='api_home'),
    url(r'user/get', get_user, name="get_user"),
    url(r'user/register', register_user, name="register_user"),
    url(r'productos', get_productos, name="get_productos"),
    url(r'producto', get_producto, name="get_producto"),

]