from django.db import models

class Departamento(models.Model):
    """
    Modelo que representa un Departamento dado, incluyendo su
    nombre, su código y el profesor que lo dirige
    como jefe del Departamento.
    """

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=2, unique=True)
    jefe = models.ForeignKey('Profesor')

class Profesor(models.Model):
    pass
