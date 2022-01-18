from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductoList, ComentarioList, ProductoTalleList, ProductosTalleList, \
    UserProfileViewSet, UserLoginApiView, api_root # UserCreate, UserList,



router = DefaultRouter()
router.register('users', UserProfileViewSet, basename='users-list')

urlpatterns = [
    path('', api_root),

    path(r'comentarios/', ComentarioList.as_view(), name="get_comentario"),

    path(r'productos/', ProductoList.as_view(), name="get_producto"),
    path(r'productos-talle/', ProductosTalleList.as_view(), name="get_productos_talle"),
    path("productos/<int:pk>/producto-talle/", ProductoTalleList.as_view(), name="get_producto_talle"),

    # path(r'users/get', UserList.as_view(), name="user_get"),
    # path(r'users/post', UserCreate.as_view(), name="user_post"),
    path(r'', include(router.urls), name='users-list'),

    path("login/", UserLoginApiView.as_view(), name="api_login"),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
