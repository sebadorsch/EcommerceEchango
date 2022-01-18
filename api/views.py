from django.shortcuts import render
from django.contrib.auth import authenticate
from Echango import models
from usuarios import models as umodels
from api import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import generics, status, filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductoSerializer, ComentarioSerializer, ProductoTalleSerializer, UserSerializer


"""
Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
Use generics.* when you only want to allow some operations on a model
Use APIView when you want to completely customize the behaviour.
"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request, format=None):
    return Response({
        'login': reverse('api_login', request=request, format=format),
        # 'users': reverse('users-list', request=request, format=format),
        'productos': reverse('get_producto', request=request, format=format),
        'productos-talle': reverse('get_productos_talle', request=request, format=format),
        'comentarios': reverse('get_comentario', request=request, format=format),
    })


class ComentarioList(generics.ListCreateAPIView):
    """ Crear y actualizar Comentarios """

    serializer_class = ComentarioSerializer
    queryset = models.Comentario.objects.all()


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
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


class ProductosTalleList(generics.ListCreateAPIView):
    """ Crear y actualizar lista ProductoTalle """

    queryset = models.ProductoTalle.objects.all()
    serializer_class = ProductoTalleSerializer


# class UserCreate(generics.CreateAPIView):
#     """ Crear Usuario """
#
#     authentication_classes = ()
#     permission_classes = [permissions.UpdateOwnProfile]
#     serializer_class = UserSerializer
#
#
# class UserList(generics.ListAPIView):
#     """ Listar Usuarios """
#
#     serializer_class = UserSerializer
#     queryset = umodels.UserProfile.objects.all()
#     permission_classes = [permissions.UpdateOwnProfile]


class UserLoginApiView(ObtainAuthToken):
    """ Crea tokens de autenticacion de Usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """ CRUD Usuario """

    # authentication_classes = ()
    # permission_classes = ()
    serializer_class = UserSerializer
    queryset = umodels.UserProfile.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (permissions.UpdateOwnProfile, )
    permission_classes = [permissions.UpdateOwnProfile, IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter, )
    search_fields = 'email'
