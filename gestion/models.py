from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Módulo que incluye los modelos a utilizar en el
Sistema de Inscripción de Postgrado Online (SIP-Online).

Incluye modelos para representar departamentos, profesores,
asignaturas y otros modelos auxiliares que se referencian entre sí.
"""

class Departamento(models.Model):
    """
    Modelo que representa un Departamento dado, incluyendo su
    nombre, su código y el profesor que lo dirige
    como jefe del Departamento.
    """

    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=2, unique=True)
    jefe = models.ForeignKey('Profesor', related_name="jefe_de", null=True)

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según su código
        ordering = ["codigo"]

    def __str__(self):
        """
        Muestra la instancia de Departamento como
        nombre (codigo)
        """

        return self.nombre + " " + "(" + self.codigo + ")"

    def tiene_jefe(self):
        """
        Determina si un Departamento tiene un jefe asociado.
        """

        return bool(self.jefe)

    def jefe_coherente(self):
        """
        Determina si el jefe del Departamento tiene coherencia
        con su Departamento asociado, es decir, que un jefe pertenezca
        al mismo Departamento que dirige.
        """

        if not self.tiene_jefe():
            raise ValueError(
                "No se puede verificar la coherencia en la jefatura de un Departamento sin jefe."
            )

        return self.jefe.departamento == self

class Profesor(models.Model):
    """
    Modelo que representa un profesor de la USB
    incluye su nombre, apellido, cedula, email, disponibilidad semanal, departamento
    y las asignaturas que puede dar.
    """

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=12, unique=True)
    disponibilidad = models.ManyToManyField('Disponibilidad', blank=True)
    departamento = models.ForeignKey('Departamento')
    email = models.EmailField(max_length=200)
    asignaturas = models.ManyToManyField('Asignatura', blank=True)

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según su cédula
        ordering = ["cedula"]

    def __str__(self):
        """
        Muestra la instancia de Profesor como
        nombre apellido
        """
        return self.nombre + " " + self.apellido

class Asignatura(models.Model):
    """
    Modelo TEMPORAL que representa una asignatura con su
    nombre, código y departamento asociado. Este modelo
    deberá ser modificado posteriormente para incorporarse
    con el desarrollo del equipo Delta Developers.
    """

    nombre = models.CharField(max_length=60)
    codigo_interno = models.CharField(max_length=4, unique=True)
    departamento = models.ForeignKey('Departamento')

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según el departamento, luego según su
        # código inerno
        ordering = ["departamento", "codigo_interno"]

    def codigo_completo(self):
        """
        Devuelve el código completo (compuesto) de la asignatura,
        que es el código del departamento y el código interno de la
        asignatura.
        """
        return self.departamento.codigo + self.codigo_interno

    def __str__(self):
        """
        Muestra la instancia de Asignatura como
        (codigodptocodigointernoasigntura) nombre
        """
        return "(" + self.codigo_completo() + ") " + self.nombre

class Disponibilidad(models.Model):
    """
    Modelo auxiliar que representa un horario (día, bloque) de
    disponibilidad para un profesor.
    """

    LUNES = (1, 'Lunes')
    MARTES = (2, 'Martes')
    MIERCOLES = (3, 'Miércoles')
    JUEVES = (4, 'Jueves')
    VIERNES = (5, 'Viernes')
    SABADO = (6, 'Sábado')

    DIA_CHOICES = (
        LUNES,
        MARTES,
        MIERCOLES,
        JUEVES,
        VIERNES,
        SABADO
    )

    bloque = models.IntegerField(
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    dia = models.IntegerField(
        choices=DIA_CHOICES,
        validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ]
    )

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según el día, y luego según el bloque
        ordering = ["dia", "bloque"]

    def __str__(self):
        return self.get_dia_display() + ", bloque " + str(self.bloque)
