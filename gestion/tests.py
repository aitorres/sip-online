# encoding=utf-8

"""
Módulo de pruebas unitarias para el entorno de desarrollo Django
que utiliza una versión de PyUnit adaptada al framework y
ya incluida para realizar las pruebas de los modelos y funciones
asociadas.
"""

from django.test import TestCase
from gestion.models import Profesor

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
        Profesor.objects.create(
            nombre="Andrés",
            apellido="Medina",
            email="14-11082@usb.ve",
            ci="V-22.252.123"
        )
        Profesor.objects.create(
            nombre="María",
            apellido="Jaimes",
            email="12-10042@usb.ve",
            ci="V-25.766.738"
        )


    def test_nombre_profesor(self):
        """
        PRUEBA 1. Se verifica que se guarde el nombre del profesor
        en la entidad, y que luego corresponda con el nombre guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        """
        profesor1 = Profesor.objects.get(ci="V-22.252.123")
        profesor2 = Profesor.objects.get(ci="V-25.766.738")

        self.assertEqual(profesor1.nombre, "Andrés")
        self.assertEqual(profesor2.nombre, "María")

    def test_apellido_profesor(self):
        """
        PRUEBA 2. Se verifica que se guarde el apellido del profesor
        en la entidad, y que luego corresponda con el apellido guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        """

        profesor1 = Profesor.objects.get(ci="V-22.252.123")
        profesor2 = Profesor.objects.get(ci="V-25.766.738")

        self.assertEqual(profesor1.apellido, "Medina")
        self.assertEqual(profesor2.apellido, "Jaimes")

    def test_email_profesor(self):
        """
        PRUEBA 3. Se verifica que se guarde el correo electrónico (email) del
        profesor en la entidad, y que luego el correo guardado corresponda
        con el apellido guardado.
        """

        profesor1 = Profesor.objects.get(ci="V-22.252.123")
        profesor2 = Profesor.objects.get(ci="V-25.766.738")

        self.assertEqual(profesor1.email, "14-11082@usb.ve")
        self.assertEqual(profesor2.email, "12-10042@usb.ve")
