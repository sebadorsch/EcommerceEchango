from django.conf.urls import url
from django.http import JsonResponse
from api.views import api_home, User, RegistroUsuario, Productos, Producto

urlpatterns = [
    url(r'^$', api_home, name='api_home'),
    url(r'user/get', User.as_view(), name="get_user"),
    url(r'user/register', RegistroUsuario.as_view(), name="register_user"),
    url(r'productos', Productos.as_view(), name="get_productos"),
    url(r'producto', Producto.as_view(), name="get_producto"),

]