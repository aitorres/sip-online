# encoding=utf-8

"""
Comando personalizado de administración de Django para asignar un profesor
ya registrado como Coordinador de alguna Coordinación existente.
"""

from gestion.models import Profesor, Coordinacion
from django.core.management.base import BaseCommand
import re

class Command(BaseCommand):
    help = 'Asigna un profesor (nuevo) como coordinador de una Coordinación (ya existente)'

    def email_valido(self, email):
        """
        Determina si una string pasada como parámetro corresponde a un e-mail válido
        siguiendo el formato estándar.
        """

        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return True
        return False

    def add_arguments(self, parser):
        """
        Agrega argumentos (opcionales) al comando para ser utilizado.
        """
        # Argumentos opcionales
        parser.add_argument(
            '-c',
            '--coord',
            type=str,
            help='Código de la Coordinación al que se le asignará el profesor'
        )

        parser.add_argument(
            '-e',
            '--email',
            type=str,
            help='E-mail del nuevo Coordinador'
        )

        parser.add_argument(
            '-c',
            '--coord',
            type=str,
            help='Código de la Coordinación'
        )

    def handle(self, *args, **kwargs):
        """
        Procedimiento que incorpora la lógica del comando de administración de Django
        que se está definiendo
        """

        email = kwargs['email']
        coord = kwargs['coord']

        if not coord:
            coord = input(
                "Introduce el código de la Coordinación que dirigirá el usuario (e.g. 'LIT' sin las comillas): "
            )

        coord = str(coord).upper()

        try:
            instancia_coord = Coordinacion.objects.get(codigo=coord)
        except:
            print("ERROR: El código introducido es incorrecto.")
            return

        if not email:
            email = input(
                "Introduce el e-mail del Profesor (NUEVO) que ahora será " + \
                "jefe del Departamento (e.g. 'adiserio@usb.ve' sin las comillas): "
            )

        if not self.email_valido(email):
            print("ERROR: El e-mail introducido no está en un formato correcto.")
            return

        try:
            instancia_profesor = Profesor.objects.get(email=email)
        except:
            print("ERROR: El e-mail introducido no corresponde a un usuario registrado.")
            return

        instancia_coord.coordinador = instancia_profesor
        instancia_coord.save()

        print(
            "El profesor %s ha sido asignado como el nuevo coordinador de la %s." % (
                instancia_profesor,
                instancia_coord
            )
        )
        return
