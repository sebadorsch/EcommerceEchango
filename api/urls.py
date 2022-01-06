from django.urls import path, include

from api.views import ProductoList, ComentarioList, ProductoTalleList, UserCreate, UserList, LoginView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path("productos/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),
    path(r'productos', ProductoList.as_view(), name="get_producto"),

    path(r'comentarios', ComentarioList.as_view(), name="get_comentario"),

    path(r'user/post', UserCreate.as_view(), name="user_list"),
    path(r'user/get', UserList.as_view(), name="user_list"),
    path(r'', include(router.urls)),

    path("login/", LoginView.as_view(), name="api_login"),
]