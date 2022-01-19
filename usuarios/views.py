from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm
from django.views import generic
from api.serializers import UserSerializer
from rest_framework import generics
from usuarios import models as umodels
from api import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters


class RegistroUsuario(generic.CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')


class CreateUserView(generics.CreateAPIView):
    """ Crear nuevo usuario en el sistema """

    serializer_class = UserSerializer
    queryset = umodels.User.objects.all()
    permission_classes = [permissions.UpdateOwnProfile, IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = 'email'


"""
class LoginUsuario(generic.CreateView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

"""
