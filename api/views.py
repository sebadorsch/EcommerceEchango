from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers


def api_home(request, template_name='index_api.html'):
    return render(request, template_name)


class User(APIView):
    """API View de Usuario"""

    def get(self, request):
        """ Retornar Usuario segun id """
        from django.contrib.auth.models import User

        data_response = {
            'status': 200,
            'response': {}
        }

        uid = request.GET.get('uid')
        usuario = User.objects.get(pk=uid)
        data_response['response'].update(
            {
            'username': usuario.username,
            }
        )

        return Response(data_response)


class RegistroUsuario(APIView):
    """API View para registrar Usuario"""
    serializers_class = serializers.RegisterUser

    def post(self, request, status=None):
        """ Registrar Usuario segund datos pasados por request """
        from usuarios.forms import RegistroUsuarioForm

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            nombre = serializer.validated_data.get('nombre')
            apellido = serializer.validated_data.get('apellido')

            data_response = {
                'status': 200,
                'response': {
                    'email': email,
                    'nombre': nombre,
                    'apellido': apellido,
                }
            }
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data_response)


class Producto(APIView):
    """API View de Producto"""

    def get(self, request, format=None):
        """Retornar un Producto"""
        from Echango.models import Producto

        data_response = {
            'status': 200,
            'response': {}
        }
        try:
            pid = request.GET.get('pid')
            producto = get_object_or_404(Producto, pk=pid)

            data_response['response'].update(
                {
                    'titulo': producto.titulo,
                    'genero': producto.genero,
                    'categoria': producto.categoria,
                    'marca': producto.marca,
                    'color': producto.color,
                    'precio': producto.precio,
                    'fecha_publicacion': producto.titulo,
                    'hora_publicacion': producto.titulo
                }
            )
        except:
            data_response = {
                'status': 403,
                'response':
                    {
                        'status': 403,
                        'error': 'Invalid PID'
                    }
            }
            return Response(data_response)

        return Response(data_response)


class Productos(APIView):
    """API View de Productos"""

    def get(self, request, format=None):
        """Retornar una lista de todos los Productos"""
        from Echango.models import Producto

        data_response = {
            'status': 200,
            'response': {}
        }
        try:
            productos = Producto.objects.all()
            data_response = {'status': 200,
                            "response": list(productos.values("titulo", "genero", "categoria",
                                                              "marca", "color", "precio",
                                                              "fecha_publicacion", "hora_publicacion"))}

        except:
            data_response = {
                'status': 403,
                'response':
                    {
                        'status': 403,
                        'error': 'Invalid PID'
                    }
            }
            return Response(data_response)

        return Response(data_response)




