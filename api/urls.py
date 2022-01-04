from django.urls import path

from api.views import api_home
from api.views import ProductoList, ComentarioList, ProductoTalleList, UserCreate, UserList

urlpatterns = [
    path(r'^$', api_home, name='api_home'),
    path("productos/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),
    path(r'productos', ProductoList.as_view(), name="get_producto"),
    path(r'comentarios', ComentarioList.as_view(), name="get_comentario"),
    path(r'users/post', UserCreate.as_view(), name="user_list"),
    path(r'users/get', UserList.as_view(), name="user_list"),
]