# encoding=utf-8

"""
Comando personalizado de administración de Django para listar las Coordinaciones
existentes.
"""

from gestion.models import Coordinacion
from django.core.management.base import BaseCommand
import re

class Command(BaseCommand):
    help = 'Lista las Coordinaciones cargadas en sistema'


    def handle(self, *args, **kwargs):
        """
        Procedimiento que incorpora la lógica del comando de administración de Django
        que se está definiendo
        """

        coordinaciones = Coordinacion.objects.all()

        if len(coordinaciones) == 0:
            print("No se han cargado coordinaciones aún.")
            print("Prueba cargando los datos iniciales con:\tpython manage.py loaddata gestion/fixtures/fixtures.json")
        else:
            for coordinacion in coordinaciones:
                print("%s (código: %s)" % (coordinacion, coordinacion.codigo))
        return
