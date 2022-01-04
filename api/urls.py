from django.urls import path

from api.views import api_home
from api.views import ProductoList, ComentarioList, ProductoTalleList, UserList

urlpatterns = [
    path(r'^$', api_home, name='api_home'),
    path("producto/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),
    path(r'producto', ProductoList.as_view(), name="get_producto"),
    path(r'comentarios', ComentarioList.as_view(), name="get_comentario"),
    path(r'users', UserList.as_view(), name="user_list"),
]