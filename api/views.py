from django.shortcuts import render

from rest_framework import generics

from .serializers import ProductoSerializer, ComentarioSerializer, ProductoTalleSerializer, UserSerializer
from Echango import models
from usuarios import models as umodels


def api_home(request, template_name='index_api.html'):
    return render(request, template_name)


class ComentarioList(generics.ListCreateAPIView):
    """ Crear y actualizar Comentarios """

    serializer_class = ComentarioSerializer
    queryset = models.Comentario.objects.all()


class ProductoList(generics.ListCreateAPIView):
    """ Crear y actualizar Productos """

    serializer_class = ProductoSerializer
    queryset = models.Producto.objects.all()


class ProductoTalleList(generics.ListCreateAPIView):
    """ Crear y actualizar ProductoTalle """

    serializer_class = ProductoTalleSerializer
    queryset = models.ProductoTalle.objects.all()


class UserList(generics.ListCreateAPIView):
    """ Listar Usuarios """

    serializer_class = UserSerializer
    queryset = umodels.User.objects.all()
