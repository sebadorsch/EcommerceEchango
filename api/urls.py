from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductoList, ComentarioList, ProductoTalleList, ProductosTalleList, \
    UserViewSet, UserLoginApiView, api_root # UserCreate, UserList,


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', api_root),

    path(r'comentarios/', ComentarioList.as_view(), name="get_comentario"),

    path(r'productos/', ProductoList.as_view(), name="get_producto"),
    path(r'productos-talle/', ProductosTalleList.as_view(), name="get_productos_talle"),
    path(r'productos/<int:pk>/producto-talle/', ProductoTalleList.as_view(), name="get_producto_talle"),

    path(r'', include(router.urls), name='users'),

    path("login/", UserLoginApiView.as_view(), name="api_login"),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
