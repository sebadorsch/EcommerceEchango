from rest_framework import serializers


class RegisterUser(serializers.Serializer):
    """ Serializa un Registro de Usuario """

    nombre = serializers.CharField(max_length=40)
    apellido = serializers.CharField(max_length=40)
    email = serializers.EmailField(max_length=60)