# encoding=utf-8

"""
Comando personalizado de administración de Django para listar los Departamentos
existentes.
"""

from gestion.models import Departamento
from django.core.management.base import BaseCommand
import re

class Command(BaseCommand):
    help = 'Lista los Departamentos cargados en sistema'


    def handle(self, *args, **kwargs):
        """
        Procedimiento que incorpora la lógica del comando de administración de Django
        que se está definiendo
        """

        departamentos = Departamento.objects.all()

        if len(departamentos) == 0:
            print("No se han cargado departamentos aún.")
            print("Prueba cargando los datos iniciales con:\tpython manage.py loaddata gestion/fixtures/fixtures.json")
        else:
            for departamento in departamentos:
                print("%s (código: %s)" % (departamento, departamento.codigo))
        return
