from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """ Testear API publica del usuario """

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_succes(self):
        """ Test creacion usuario con un payload exitoso """

        payload = {
            'email': 'test@testing.com',
            'password': 'passwordtest',
            'nombre': 'nombretest',
            'apellido': 'apellidotest'
        }

        res = self.client.post('/api/users/', payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """ Test creacion usuario ya existente """

        payload = {
            'email': 'test@testing.com',
            'password': 'passwordtest',
            'nombre': 'nombretest',
            'apellido': 'apellidotest'
        }
        create_user(**payload)

        res = self.client.post('/api/users/', payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """ Test contraseña debe ser mayor a 5 caracteres """

        payload = {
            'email': 'test@testing.com',
            'password': 'test',
            'nombre': 'nombretest',
            'apellido': 'apellidotest'
        }
        res = self.client.post('/api/users/', payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exist = get_user_model().objects.filter(email=payload['email']).exists()

        self.assertFalse(user_exist)