from django.urls import path
from usuarios.views import RegistroUsuario

urlpatterns = [
    path('registro', RegistroUsuario.as_view(), name='registro'),
]
