from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)
    mail = models.CharField(max_length=50, null=True, blank=True)
    saldo = models.FloatField(null=True, blank=True)