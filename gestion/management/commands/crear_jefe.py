# encoding=utf-8

"""
Comando personalizado de administración de Django para crear un profesor
nuevo como Jefe del Departamento de algún Departamento existente.
"""

from gestion.models import Profesor, Departamento
from django.core.management.base import BaseCommand
import re

class Command(BaseCommand):
    help = 'Asigna un profesor (nuevo) como jefe de un Departamento (ya existente)'

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
                "Introduce el e-mail del Profesor (NUEVO) que ahora será " + \
                "jefe del Departamento (e.g. 'adiserio@usb.ve' sin las comillas): "
            )

        if not self.email_valido(email):
            print("ERROR: El e-mail introducido no está en un formato correcto.")
            return

        nombre = input(
            "Introduce el nombre del Profesor: "
        )
        apellido = input(
            "Introduce el apellido del Profesor: "
        )
        ci = input(
            "Introduce la cédula del profesor (formato: V-00000000): "
        )

        try:
            instancia_profesor = Profesor.objects.get(email=email)
            print("ERROR: El e-mail introducido corresponde a un usuario registrado.")
            return
        except:
            instancia_profesor = Profesor.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                cedula=ci,
                departamento=instancia_dpto
            )

        instancia_dpto.jefe = instancia_profesor
        instancia_dpto.save()
        print(
            "El profesor %s ha sido asignado como el nuevo jefe del %s." % (
                instancia_profesor,
                instancia_dpto
            )
        )
        return
