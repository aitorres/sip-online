# encoding=utf-8

"""
Comando personalizado de administración de Django para asignar un profesor
ya registrado como Jefe del Departamento de algún Departamento existente.
"""

from gestion.models import Profesor, Departamento
from django.core.management.base import BaseCommand
import re

class Command(BaseCommand):
    help = 'Asigna un profesor (ya existente) como jefe de un Departamento (ya existente)'

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
            '-d',
            '--dpto',
            type=str,
            help='Código del Departamento al que se le asignará el jefe'
        )

        parser.add_argument(
            '-e',
            '--email',
            type=str,
            help='E-mail del nuevo Jefe del Departamento'
        )

    def handle(self, *args, **kwargs):
        """
        Procedimiento que incorpora la lógica del comando de administración de Django
        que se está definiendo
        """

        email = kwargs['email']
        dpto = kwargs['dpto']

        if not dpto:
            dpto = input(
                "Introduce el código del Departamento a modificar (e.g. 'CI' sin las comillas): "
            )

        dpto = str(dpto).upper()

        try:
            instancia_dpto = Departamento.objects.get(codigo=dpto)
        except:
            print("ERROR: El código introducido es incorrecto.")
            return

        if not email:
            email = input(
                "Introduce el e-mail del Profesor (YA REGISTRADO EN SISTEMA) que ahora será " + \
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

        if instancia_profesor.departamento != instancia_dpto:
            print("ERROR: El profesor escogido no es parte del Departamento seleccionado.")
            return

        instancia_dpto.jefe = instancia_profesor
        instancia_dpto.save()
        print(
            "El profesor %s ha sido asignado como el nuevo jefe del %s." % (
                instancia_profesor,
                instancia_dpto
            )
        )
        return
