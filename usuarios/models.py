from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager de la clase Usuario"""

    def create_user(self, email, nombre, apellido, password=None):
        """ Crear nuevo User"""
        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, apellido=apellido)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nombre, apellido, password):
        """ Crear nuevo SuperUser"""
        user = self.create_user(email, nombre, apellido, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo Base de Datos para Usuarios del sistema """
    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.email

    def get_nombre(self):
        return self.nombre

    def get_nombre_apellido(self):
        return f"{self.nombre} {self.apellido}"




