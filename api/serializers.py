from rest_framework import serializers
from Echango.models import Producto, ProductoTalle, Comentario
from usuarios.models import User


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
        # fields = ('titulo', 'descripcion', 'genero', 'categoria',
        #           'marca', 'color', 'precio', 'publicado')

    # def create(self, validated_data):
    #     """ Crea y retorna un nuevo Producto """
    #     producto=Producto.objects.create(
    #         titulo=validated_data['titulo'],
    #         descripcion=validated_data['descripcion'],
    #         genero=validated_data['genero'],
    #         categoria=validated_data['categoria'],
    #         marca=validated_data['marca'],
    #         color=validated_data['color'],
    #         precio=validated_data['precio'],
    #         publicado=validated_data['publicado'],
    #     )


class ProductoTalleSerializer(serializers.ModelSerializer):
    """ Serializa el objeto ProductoTalle """

    class Meta:
        model = ProductoTalle
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """ Serializa el objecto User """

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
