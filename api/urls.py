from django.urls import path, include

from api.views import ProductoList, ComentarioList, ProductoTalleList, UserCreate, UserList, LoginView, UserProfileViewSet, UserLoginApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserProfileViewSet, basename='user')

urlpatterns = [
    path(r'comentarios', ComentarioList.as_view(), name="get_comentario"),

    path("productos/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),
    path(r'productos', ProductoList.as_view(), name="get_producto"),

    path(r'user/post', UserCreate.as_view(), name="user_post"),
    path(r'user/get', UserList.as_view(), name="user_get"),
    path(r'', include(router.urls)),

    path("login/", UserLoginApiView.as_view(), name="api_login"),
]