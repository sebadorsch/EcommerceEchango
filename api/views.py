from django.shortcuts import render

from rest_framework import generics

from .serializers import ProductoSerializer, ComentarioSerializer, ProductoTalleSerializer, UserSerializer
from Echango import models
from usuarios import models as umodels

"""
Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
Use generics.* when you only want to allow some operations on a model
Use APIView when you want to completely customize the behaviour.
"""


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

    # queryset = models.ProductoTalle.objects.all()
    def get_queryset(self):
        queryset = models.ProductoTalle.objects.all().filter(producto_id=self.kwargs['pk'])
        return queryset
    serializer_class = ProductoTalleSerializer


class UserList(generics.ListCreateAPIView):
    """ Listar Usuarios """

    serializer_class = UserSerializer
    queryset = umodels.User.objects.all()
