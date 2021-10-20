from django.urls import path
from usuarios.views import RegistroUsuario#, LoginUsuario

urlpatterns = [
    path('registro', RegistroUsuario.as_view(), name='registro'),
    #path('login', LoginUsuario.as_view(), name='login'),
]
