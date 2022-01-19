from django.urls import path
from usuarios.views import RegistroUsuario, CreateUserView

urlpatterns = [
    path('registro', RegistroUsuario.as_view(), name='registro'),
    path('create/', CreateUserView.as_view(), name='create_user')
]
