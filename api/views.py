from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, template_name='index_api.html'):
    return render(request, template_name)


def get_user(request):
    from django.contrib.auth.models import User

    data_response = {
        'status': 200,
        'response':
            {
            }
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
                     'mensaje': 'Invalid UID',
                     'causa': ['El UID del usuario no es valido'],
                     'error': 'Invalid UID'
                 }
             }
        return JsonResponse(data_response)

    return JsonResponse(data_response)