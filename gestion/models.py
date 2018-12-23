from django.db import models
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.template import loader
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

"""
Módulo que incluye los modelos a utilizar en el
Sistema de Inscripción de Postgrado Online (SIP-Online).

Incluye modelos para representar departamentos, profesores,
asignaturas y otros modelos auxiliares que se referencian entre sí.
"""

def _enviar_correo(para, asunto, plantilla_mensaje, contexto):
    """
    Función privada para enviar un correo electrónico a los profesores
    según sea necesario.
    """

    mensaje = loader.render_to_string(
        plantilla_mensaje,
        contexto
    )

    return send_mail(
        asunto,
        mensaje,
        "SIP Online <no-reply@sip-online.com>",
        [para],
        fail_silently=False,
    )

class Departamento(models.Model):
    """
    Modelo que representa un Departamento dado, incluyendo su
    nombre, su código y el profesor que lo dirige
    como jefe del Departamento.
    """

    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=2, unique=True)
    jefe = models.OneToOneField('Profesor', related_name="jefe_de", null=True, on_delete=models.SET_NULL) 

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

class Coordinacion(models.Model):
    """
    Modelo que representa una Coordinacion dada, incluyendo su
    nombre, sus asignaturas asociadas y el profesor que lo dirige
    como coordinador.
    """

    nombre = models.CharField(max_length=200, unique=True)
    codigo = models.CharField(max_length=3, unique=True)
    asignaturas = models.ManyToManyField('Asignatura', blank=True)
    coordinador = models.ForeignKey('Profesor', null=True, on_delete=models.SET_NULL)

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según su nombre
        ordering = ["nombre"]

    def __str__(self):
        """
        Muestra la instancia de Coordinacion como
        nombre
        """

        return self.nombre

    def tiene_coordinador(self):
        """
        Determina si una Coordinacion  tiene un coordinador asociado.
        """

        return bool(self.coordinador)

    def ofertas_disponibles(self):
        """
        Devuelve las ofertas trimestrales finales a la que la Coordinación tiene
        acceso.
        """

        # Obtenemos todas las ofertas finales, y las asignaturas de
        # interés para la Coordinación
        ofertas_finales = OfertaTrimestral.objects.filter(es_final=True)
        asignaturas_de_interes = self.asignaturas.all()

        # Iteramos por cada oferta final disponible
        ofertas_disponibles = set()

        for oferta in ofertas_finales:
            # Obtenemos la intersección entre las asignaturas
            asignaturas_ofertadas = oferta.asignaturas_ofertadas()

            for asignatura in asignaturas_ofertadas:
                asignaciones_finales = AsignacionProfesoral.objects.filter(
                    es_final=True,
                    oferta_trimestral=oferta,
                    asignatura=asignatura
                )

                if asignatura in asignaturas_de_interes and len(asignaciones_finales) > 0:
                    ofertas_disponibles.add(oferta)
                    break

        return ofertas_disponibles

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
    email = models.EmailField(max_length=200, unique=True)
    asignaturas = models.ManyToManyField('Asignatura', blank=True)
    usuario = models.OneToOneField(User, blank=True, default=None, null=True)

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según su cédula
        ordering = ["cedula"]

    def es_jefe(self):
        """
        Determina si un profesor es jefe de su departamento asignado.
        """

        return self.departamento.jefe == self

    def es_coordinador(self):
        """
        Determina si un profesor es coordinador de alguna Coordinación.
        """

        coordinaciones = Coordinacion.objects.filter(coordinador=self)

        return len(coordinaciones) != 0

    def coordinacion(self):
        """
        Retorna la coordinación a la que está asociado el coordinador
        """

        coordinaciones = Coordinacion.objects.filter(coordinador=self)

        if len(coordinaciones) == 1:
            return coordinaciones.first()
        return None

    def __str__(self):
        """
        Muestra la instancia de Profesor como
        nombre apellido
        """
        return self.nombre + " " + self.apellido

class Asignatura(models.Model):
    """
    Modelo que representa una asignatura con su
    nombre, código y departamento asociado.
    """

    nombre = models.CharField(max_length=60, verbose_name="Nombre de la asignatura")
    codigo_interno = models.CharField(max_length=4, unique=True, verbose_name="Código interno")
    departamento = models.ForeignKey('Departamento', verbose_name="Departamento asociado")
    horas_laboratorio = models.IntegerField(default=0, verbose_name="Horas de Laboratorio")
    horas_teoria = models.IntegerField(default=0, verbose_name="Horas de Teoría")
    horas_practica = models.IntegerField(default=0, verbose_name="Horas de Práctica")
    unidad_creditos = models.IntegerField(default=0, verbose_name="Unidades de Crédito (U.C.)")
    requisitos = models.ManyToManyField('Asignatura', blank=True, verbose_name="Requisitos")

    class Meta:
        """
        Provee algunas configuraciones básicas con respecto a las
        operaciones del modelo.
        """

        # Ordenamiento por defecto: según el departamento, luego según su
        # código inerno
        ordering = ["departamento", "codigo_interno"]

    def tiene_requisito(self):
        """
        Determina si una asignatura tiene un requisito.
        """

        return bool(self.requisitos.all())

    def codigo_completo(self):
        """
        Devuelve el código completo (compuesto) de la asignatura,
        que es el código del departamento y el código interno de la
        asignatura.
        """
        return self.departamento.codigo + self.codigo_interno

    def horas_l(self):
    	"""
    	Devuelve la cantidad de horas de laboratorio de
    	la asignatura
    	"""
    	return self.horas_laboratorio

    def horas_p(self):
    	"""
    	Devuelve la cantidad de horas de practica de
    	la asignatura
    	"""
    	return self.horas_practica

    def horas_t(self):
    	"""
    	Devuelve la cantidad de horas de teoria de
    	la asignatura
    	"""
    	return self.horas_teoria

    def creditos(self):
    	"""
		Devuelve el valor de unidad_creditos de la asignatura
    	"""
    	return self.unidad_creditos

    def profesores(self):
        """
        Devuelve un conjunto de los profesores que dictan esta asignatura.
        """

        lista_profesores = set()
        profes = Profesor.objects.all()
        for prof in profes:
            if self in prof.asignaturas.all():
                lista_profesores.add(prof)

        return lista_profesores

    def horarios(self):
        profesores = self.profesores()
        disponibilidades = set()

        for profesor in profesores:
            for momento in profesor.disponibilidad.all():
                disponibilidades.add(momento.identificador_unico())
        
        return disponibilidades

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

class OfertaTrimestral(models.Model):
    """
    Modelo que representa la oferta trimestral de un DEPARTAMENTO con los datos sobre:
    El codigo de la forma XX00, donde la X representan la letra del trimestre por ejemplo EM
    y los 00 representan el año, por ejemplo 18. Teniendo asi como trimestre EM18.
    El campo es_final, de tipo booleano, indica si la oferta es final o no.
    """

    trimestre = models.CharField(max_length=4)
    departamento = models.ForeignKey(
        "Departamento",
        on_delete=models.CASCADE
    )
    es_final = models.BooleanField(default=False)

    class Meta:
        """
        Determina algunas opciones base para el modelo Oferta Trimestral.
        """

        # Restricción de unicidad conjunta entre trimestre y departamento
        unique_together = ('trimestre', 'departamento',)

    def nombre_completo(self):
        """
        Retorna el nombre completo de un trimestre reconstruyéndolo a partir
        de su código.
        """

        NOMBRES = {
            'EM': "Enero - Marzo",
            'AJ': "Abril - Julio",
            'JA': "Julio - Agosto",
            'SD': "Septiembre - Diciembre"
        }

        # Obtenemos el trimestre a partir del código de período
        codigo_periodo = self.trimestre[0:2]
        nombre_trimestre = NOMBRES[codigo_periodo]

        # Obtenemos el año, entre 2000 y 2099
        ano = "20" + self.trimestre[2:]

        nombre_completo = "%s %s" % (nombre_trimestre, ano)
        return nombre_completo

    def estado(self):
        """
        Retorna una representación en cadena de caracteres del estado
        de la oferta trimestral.
        """

        estado = "final" if self.es_final else "preliminar"
        return estado

    def asignaturas_ofertadas(self):
        """
        Retorna un queryset que incluye todas las asignaturas ofertadas en un trimestre
        según la asignación profesoral.
        """

        asignaciones = AsignacionProfesoral.objects.filter(oferta_trimestral=self)
        asignaturas = set(
            [asignacion.asignatura for asignacion in asignaciones]
        )

        return asignaturas

    def profesores_ofertados(self):
        """
        Retorna un queryset que incluye todos los profesores ofertados en un trimestre
        según la asignación profesoral.
        """

        asignaciones = AsignacionProfesoral.objects.filter(oferta_trimestral=self)
        profesores = set(
            [asignacion.profesor for asignacion in asignaciones]
        )

        return profesores

    def __str__(self):
        """
        Retorna una representación como cadena de caracteres de la oferta trimestral.
        """

        return self.nombre_completo()


class AsignacionProfesoral(models.Model):
    """
    Modelo que representa una asignación de una asignatura en un trimestre a un profesor de la USB.
    Incluye la oferta trimestral, el profesor asociado, la asignatura asociada, un campo booleano que indica si la
    asignacion es final y el campo tipo que indica la modalidad de la materia
    """

    TEORIA = 'TEO'
    PRACTICA = 'PRA'
    OTRO ='OTR'

    TIPO_CHOICES = (
        (TEORIA, 'Teoría'),
        (PRACTICA, 'Práctica'),
        (OTRO,'Otro'),
    )

    oferta_trimestral = models.ForeignKey('OfertaTrimestral')
    profesor = models.ForeignKey('Profesor')
    asignatura = models.ForeignKey('Asignatura')
    es_final = models.BooleanField(default=False)
    es_preferida = models.BooleanField(default=False)
    tipo = models.CharField(
        max_length=3,
        choices=TIPO_CHOICES,
        default=TEORIA
    )

    def __str__(self):
        periodo = str(self.oferta_trimestral)
        asignatura = str(self.asignatura)
        profesor = str(self.profesor)
        estatus = "final" if self.es_final else "preliminar"

        return "(%s) %s dictada por %s (%s)" % (
            periodo,
            asignatura,
            profesor,
            estatus
        )

@receiver(post_save, sender=Profesor)
def trigger_actualizar_profesor(sender, instance, created, **kwargs):
    """
    Trigger de la base de datos para crear un usuario asociado al profesor cuando
    se crea este mismo, o modificar los datos del usuario cuando se modifica
    el profesor.
    """

    # Marcamos la instancia recibida como profesor
    profesor = instance

    if created:
        # Creamos el usuario asociado al profesor con una contraseña aleatoria
        usuario = User.objects.create_user(
            first_name=profesor.nombre,
            last_name=profesor.apellido,
            email=profesor.email,
            username=profesor.email,
        )
        password = User.objects.make_random_password()
        usuario.set_password(password)
        usuario.save()

        # Notificamos la creación del usuario
        _enviar_correo(
            profesor.email,
            "[SIP ONLINE] Usuario creado",
            'emails/usuario_creado.html',
            {
                'password': password,
                'nombre': "%s %s" % (profesor.nombre, profesor.apellido)
            }
        )

        # Desconectamos el trigger para poder asociar el usuario al profesor
        post_save.disconnect(trigger_actualizar_profesor, sender=sender)
        profesor.usuario = usuario
        profesor.save()

        # Volvemos a conectar el trigger
        post_save.connect(trigger_actualizar_profesor, sender=sender)
    else:
        # Obtenemos el usuario ya asociado
        usuario = profesor.usuario

        # Cambiamos los datos que pudieran haber cambiado y guardamos el usuario
        usuario.first_name = profesor.nombre
        usuario.last_name = profesor.apellido
        usuario.email = profesor.email
        usuario.username = profesor.email

        usuario.save()
    return

@receiver(post_delete, sender=Profesor)
def trigger_eliminar_profesor(sender, instance, **kwargs):
    """
    Trigger de la base de datos para eliminar un usuario cuando su instancia
    de profesor asociada es eliminada también.
    """

    # Marcamos la instancia recibida como profesor
    profesor = instance

    # Obtenemos el usuario ya asociado
    usuario = profesor.usuario

    # Eliminamos el usuario y terminamos la ejecución
    usuario.delete()
    return

