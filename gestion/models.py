from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

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
    jefe = models.ForeignKey('Profesor', related_name="jefe_de", null=True, on_delete=models.SET_NULL) 

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

    def nombre_corto(self):
        """
        Retorna el nombre del Departamento sin la frase inicial
        'Departamento de'.
        """

        nombre = str(self)

        if nombre.startswith("Departamento de "):
            nombre = nombre[16:]

        return nombre

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
    usuario = models.OneToOneField(User, blank=True, default=None, null=True)

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

    def identificador_unico(self):
        """
        Retorna el identificador único numérico del bloque (dia y hora)
        según una formula biyectiva de R² a R.
        """

        cantidad_bloques = 12

        return cantidad_bloques*(self.dia-1) + self.bloque

    def matriz_bloques():
        """
        Devuelve un diccionario que contiene los valores por biyección
        asignados a cada bloque, cada valor representando un día,
        de modo que se pueda representar fácilmente la matriz de manera
        visual.
        """

        matriz_bloques = {
            1: [1, 13, 25, 36, 49, 61],
            2: [2, 14, 26, 38, 50, 62],
            3: [3, 15, 27, 39, 51, 63],
            4: [4, 16, 28, 40, 52, 64],
            5: [5, 17, 29, 41, 53, 65],
            6: [6, 18, 30, 42, 54, 66],
            7: [7, 19, 31, 43, 55, 67],
            8: [8, 20, 32, 44, 56, 68],
            9: [9, 21, 33, 45, 57, 69],
            10: [10, 22, 34, 46, 58, 70],
            11: [11, 23, 35, 47, 59, 71],
            12: [12, 24, 36, 48, 60, 72],
        }

        return matriz_bloques

    def __str__(self):
        """
        Muestra representación en cadena de caracteres del bloque de disponibilidad,
        indicando su día y luego su bloque.
        """

        return self.get_dia_display() + ", bloque " + str(self.bloque)
