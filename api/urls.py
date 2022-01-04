from django.conf.urls import url

from api.views import api_home
from api.views import ProductoList, ComentarioList, ProductoTalleList, UserList

urlpatterns = [
    url(r'^$', api_home, name='api_home'),
    url(r'productos', ProductoList.as_view(), name="get_productos"),
    url(r'comentarios', ComentarioList.as_view(), name="get_comentario"),
    url(r'producto-talle', ProductoTalleList.as_view(), name="get_producto_talle"),
    url(r'users', UserList.as_view(), name="user_list"),
]