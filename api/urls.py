from django.urls import path

from api.views import ProductoList, ComentarioList, ProductoTalleList, UserCreate, UserList, LoginView

urlpatterns = [
    path("productos/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),
    path(r'productos', ProductoList.as_view(), name="get_producto"),
    path(r'comentarios', ComentarioList.as_view(), name="get_comentario"),
    path(r'users/post', UserCreate.as_view(), name="user_list"),
    path(r'users/get', UserList.as_view(), name="user_list"),
    path("login/", LoginView.as_view(), name="login"),
]