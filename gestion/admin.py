"""
Módulo para el registro de los modelos de la base de datos
en el admin de Django para poder realizar en este sitio operaciones
sencillas de CRUD de manera fácil para el programador.
"""

from django.contrib import admin

from gestion.models import Profesor, Asignatura, Departamento, Disponibilidad

admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Departamento)
admin.site.register(Disponibilidad)
