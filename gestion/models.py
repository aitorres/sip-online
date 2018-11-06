from django.db import models

class Departamento(models.Model):
    """
    Modelo que representa un Departamento dado, incluyendo su
    nombre, su código y el profesor que lo dirige
    como jefe del Departamento.
    """

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=2, unique=True)
    jefe = models.ForeignKey('Profesor', related_name="jefe_de")

class Profesor(models.Model):
    """
    Modelo que representa un profesor de la USB
    incluye su nombre, apellido, cedula, email, disponibilidad semanal, departamento 
    y las asignaturas que puede dar.
    """

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=12, unique=True)
    #disponibilidad
    departamento = models.ForeignKey('Departamento')
    correo = models.EmailField(max_length=200)
    asignaturas = models.ManyToManyField('Asignatura')

class Asignatura(models.Model):
    pass