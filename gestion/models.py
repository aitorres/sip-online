from django.db import models

class Departamento(models.Model):
    """
    Modelo que representa un Departamento dado, incluyendo su
    nombre, su código y el profesor que lo dirige
    como jefe del Departamento.
    """

    """ 
    Muestra la instancia de Departamento como 
    nombre (codigo) 
    """
    def __str__(self):
        return (self.nombre + " " + "(" + self.codigo + ")")


    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=2, unique=True)
    jefe = models.ForeignKey('Profesor', related_name="jefe_de", null=True)

class Profesor(models.Model):
    """
    Modelo que representa un profesor de la USB
    incluye su nombre, apellido, cedula, email, disponibilidad semanal, departamento 
    y las asignaturas que puede dar.
    """

    """ 
    Muestra la instancia de Profesor como 
    nombre apellido 
    """
    def __str__(self):
        return (self.nombre + " " + self.apellido)


    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=12, unique=True)
    #disponibilidad
    departamento = models.ForeignKey('Departamento')
    email = models.EmailField(max_length=200)
    asignaturas = models.ManyToManyField('Asignatura')

class Asignatura(models.Model):
    """
    Modelo TEMPORAL que representa una asignatura con su
    nombre, código y departamento asociado. Este modelo
    deberá ser modificado posteriormente para incorporarse
    con el desarrollo del equipo Delta Developers.
    """

    """ 
    Muestra la instancia de Asignatura como 

    (codigodptocodigointernoasigntura) nombre 
    """
    def __str__(self):
        return ("(" + self.departamento.codigo + self.codigo_interno + ") " + self.nombre)

    nombre = models.CharField(max_length=60)
    codigo_interno = models.CharField(max_length=4, unique=True)
    departamento = models.ForeignKey('Departamento')
