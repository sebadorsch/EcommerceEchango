from django.shortcuts import render
from django.contrib.auth import authenticate
from Echango import models
from usuarios import models as umodels
from api import permissions

from rest_framework import generics, status, filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from .serializers import ProductoSerializer, ComentarioSerializer, ProductoTalleSerializer, UserSerializer


"""
Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
Use generics.* when you only want to allow some operations on a model
Use APIView when you want to completely customize the behaviour.
"""


class ComentarioList(generics.ListCreateAPIView):
    """ Crear y actualizar Comentarios """

    serializer_class = ComentarioSerializer
    queryset = models.Comentario.objects.all()


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


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


class UserCreate(generics.CreateAPIView):
    """ Crear Usuario """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    """ Listar Usuarios """

    serializer_class = UserSerializer
    queryset = umodels.User.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """ CRUD Usuario """

    # authentication_classes = ()
    # permission_classes = ()
    serializer_class = UserSerializer
    queryset = umodels.User.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('username', 'email')
