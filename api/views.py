from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, template_name='index_api.html'):
    return render(request, template_name)


def get_user(request):
    from django.contrib.auth.models import User

    data_response = {
        'status': 200,
        'response': {}
    }

    try:
        uid = request.GET.get('uid')
        usuario = User.objects.get(pk=uid)
        data_response['response'].update(
            {
            'username': usuario.username,
            }
        )

    except:
        data_response = {
            'status': 403,
             'response':
                 {
                     'status': 403,
                     'error': 'Invalid UID'
                 }
             }
        return JsonResponse(data_response)

    return JsonResponse(data_response)


def get_producto(request):
    from Echango.models import Producto

    data_response = {
        'status': 200,
        'response': {}
    }

    try:
        pid = request.GET.get('pid')
        producto = Producto.objects.get(pk=pid)

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
        return JsonResponse(data_response)

    return JsonResponse(data_response)

def register_user(request):
    from usuarios.forms import RegistroUsuarioForm

    data_response = {
        'status': 200,
        'response': {}
    }

    if request.method == "POST":
        print("entro")
        try:
            registro_usuario_form = RegistroUsuarioForm(username=request.username, password1=request.password,
                                                        password2=request.password, nombre=request.nombre,
                                                        apellido=request.apellido, email=request.email)

            if registro_usuario_form.is_valid():
                data_response = {
                    'status': 200,
                    'response': {
                        'username': request.username,
                        'email': request.email,
                        'nombre': request.nombre,
                        'apellido': request.apellido
                    }
                }

        except:
            data_response = {
                'status': 400,
                'response': {
                    'Error cargando los parametros'
                }
            }

        return JsonResponse(data_response)

    else:

        return "error"
