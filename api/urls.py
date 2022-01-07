from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductoList, ComentarioList, ProductoTalleList, UserCreate, \
    UserList, UserProfileViewSet, UserLoginApiView


router = DefaultRouter()
router.register('users', UserProfileViewSet, basename='user')

urlpatterns = [
    path(r'comentarios/', ComentarioList.as_view(), name="get_comentario"),

    path("productos/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),
    path(r'productos/', ProductoList.as_view(), name="get_producto"),

    path(r'users/get', UserList.as_view(), name="user_get"),
    path(r'users/post', UserCreate.as_view(), name="user_post"),
    path(r'', include(router.urls)),

    path("login/", UserLoginApiView.as_view(), name="api_login"),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]