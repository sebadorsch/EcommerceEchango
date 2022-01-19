from Echango.models import Producto, ProductoTalle, Comentario
from usuarios.models import User
from django.contrib.auth import get_user_model

from rest_framework import serializers


class ComentarioSerializer(serializers.ModelSerializer):
    """ Serializa el objeto Comentario """

    class Meta:
        model = Comentario
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    """ Serializa el objeto Producto """

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoTalleSerializer(serializers.ModelSerializer):
    """ Serializa el objeto ProductoTalle """

    class Meta:
        model = ProductoTalle
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """ Serializa el objecto User """

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'nombre', 'apellido')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """ Crear nuevo usuario con clave encriptada y retornarlo """

        return get_user_model().objects.create_user(**validated_data)
