from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        """ Test creacion nuevo Usuario con un email correctamente """
        email = 'test@prueba.com'
        password = 'Testpass123'
        nombre = 'nombreprueba'
        apellido = 'apellidoprueba'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            nombre=nombre,
            apellido=apellido
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.nombre, nombre)
        self.assertEqual(user.apellido, apellido)

    def test_new_user_email_normalized(self):
        """ Test para nuevo email de Usuario normalizado """
        email = "test@PRUEBA.COM"
        password = 'Testpass123'
        nombre = 'nombreprueba'
        apellido = 'apellidoprueba'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            nombre=nombre,
            apellido=apellido
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test para nuevo usuario con email invalido """
        password = 'Testpass123'
        nombre = 'nombreprueba'
        apellido = 'apellidoprueba'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password=password,
                nombre=nombre,
                apellido=apellido
            )

    def test_create_new_superuser(self):
        """ Test crear nuevo superusuario """
        email = "test@PRUEBA.COM"
        password = 'Testpass123'
        nombre = 'nombreprueba'
        apellido = 'apellidoprueba'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
            nombre=nombre,
            apellido=apellido
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)