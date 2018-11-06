from django.test import TestCase

from gestion.models import Profesor

class ProfesorModelTest(TestCase):

    def test_nombre_profesor(self):
        """
        PRUEBA 1. Se verifica que se guarde el nombre del profesor
        en la entidad, y que luego corresponda con el nombre guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        """

        profesor = Profesor(nombre="Andrés")
        self.assertEqual(profesor.nombre, "Andrés")

    def test_apellido_profesor(self):
        """
        PRUEBA 2. Se verifica que se guarde el apellido del profesor
        en la entidad, y que luego corresponda con el apellido guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        """

        profesor = Profesor(apellido="Medina")
        self.assertEqual(profesor.apellido, "Medina")
