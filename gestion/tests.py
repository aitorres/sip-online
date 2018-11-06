# encoding=utf-8

"""
Módulo de pruebas unitarias para el entorno de desarrollo Django
que utiliza una versión de PyUnit adaptada al framework y
ya incluida para realizar las pruebas de los modelos y funciones
asociadas.
"""

from django.test import TestCase
from gestion.models import Profesor, Departamento, Asignatura

class ProfesorModelTest(TestCase):
    """
    Suite de pruebas para el modelo Profesor, que incluye
    pruebas de frontera, de esquina y de malicia para los atributos
    del modelo Profesor, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        Profesor.objects.create(
            nombre="Andrés",
            apellido="Medina",
            email="14-11082@usb.ve",
            cedula="V-22.252.123",
            departamento=dpto_compu
        )
        Profesor.objects.create(
            nombre="María",
            apellido="Jaimes",
            email="12-10042@usb.ve",
            cedula="V-25.766.738",
            departamento=dpto_compu
        )


    def test_nombre_profesor(self):
        """
        PRUEBA 1. Se verifica que se guarde el nombre del profesor
        en la entidad, y que luego corresponda con el nombre guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        """
        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(profesor1.nombre, "Andrés")
        self.assertEqual(profesor2.nombre, "María")

    def test_apellido_profesor(self):
        """
        PRUEBA 2. Se verifica que se guarde el apellido del profesor
        en la entidad, y que luego corresponda con el apellido guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        """

        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(profesor1.apellido, "Medina")
        self.assertEqual(profesor2.apellido, "Jaimes")

    def test_email_profesor(self):
        """
        PRUEBA 3. Se verifica que se guarde el correo electrónico (email) del
        profesor en la entidad, y que luego el correo guardado corresponda
        con el apellido guardado.
        """

        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(profesor1.email, "14-11082@usb.ve")
        self.assertEqual(profesor2.email, "12-10042@usb.ve")

class DepartamentoModelTest(TestCase):
    """
    Suite de pruebas para el modelo Departamento, que incluye
    pruebas de frontera, de esquina y de malicia para los atributos
    de este modelo, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        jefe_compu = Profesor.objects.create(
            nombre="Ángela",
            apellido="Di Serio",
            email="adiserio@usb.ve",
            cedula="V-14.241.234",
            departamento=dpto_compu
        )

        dpto_compu.jefe = jefe_compu
        dpto_compu.save()        

    def test_nombre_departamento(self):
        """
        PRUEBA 1. Se verifica que el nombre del Departamento se guarde
        correctamente en la entidad, y que luego el nombre guardado
        corresponda al departamento.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no está creado.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        self.assertEqual(
            dpto_ci.nombre,
            "Departamento de Computación y Tecnología de la Información"
        )

    def test_codigo_departamento(self):
        """
        PRUEBA 2. Se verifica que el código del Departamento se guarde
        correctamente en la base de datos, y que corresponda al código
        que se quiso almacenar.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no está creado.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        self.assertEqual(
            dpto_ci.codigo, "CI"
        )

    def test_jefe_departamento(self):
        """
        PRUEBA 3. Se verifica que se asocie la cuenta de un profesor
        en la base de datos como jefe del Departamento y que sea
        el usuario que se quiso almacenar.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no está creado.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        jefe = Profesor.objects.get(email="adiserio@usb.ve")
        self.assertEqual(
            dpto_ci.jefe,
            jefe
        )

class AsignaturaModelTest(TestCase):
    """
    Suite de pruebas para el modelo Asignatura, que incluye
    pruebas de frontera, de esquina y de malicia para los atributos
    de este modelo, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        jefe_compu = Profesor.objects.create(
            nombre="Ángela",
            apellido="Di Serio",
            email="adiserio@usb.ve",
            cedula="V-14.241.234",
            departamento=dpto_compu
        )

        dpto_compu.jefe = jefe_compu
        dpto_compu.save()

        Asignatura.objects.create(
            nombre="Ingeniería de Software I",
            codigo_interno="3715",
            departamento=dpto_compu
        )

    def test_nombre_asignatura(self):
        """
        PRUEBA 1. Se verifica que el nombre de la Asignatura se guarde
        correctamente en la entidad, y que luego el nombre guardado
        corresponda al departamento.

        PRIMERA CORRIDA: Falla porque el modelo Asignatura no está creado.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            asignatura.nombre,
            "Ingeniería de Software I"
        )

    def test_codigo_departamento(self):
        """
        PRUEBA 2. Se verifica que el código interno de la Asignatura se guarde
        correctamente en la base de datos, y que corresponda al código
        que se quiso almacenar.

        PRIMERA CORRIDA: Falla porque el modelo Asignatura no está creado.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            asignatura.codigo, "CI"
        )

    def test_jefe_departamento(self):
        """
        PRUEBA 3. Se verifica que se asocie un Departamento ya existente
        como el departamento asociado de la Asignatura.

        PRIMERA CORRIDA: Falla porque el modelo Asignatura no está creado.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        dpto_compu = Departamento.objects.get(codigo="CI")
        self.assertEqual(
            asignatura.departamento,
            dpto_compu
        )
