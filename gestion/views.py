from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from gestion.models import Profesor, Asignatura, Departamento

class Dashboard(generic.TemplateView):
    """
    Controlador para el dashboard principal de la aplicación.
    Renderiza la plantilla incluyendo contadores dinámicos
    de algunas entidades de la base de datos.
    """

    template_name = "dashboard.html"

    def get_context_data(self, *args, **kwargs):
        """
        Devuelve el diccionario de contexto básico para la plantilla
        a renderizar. Incluye algunos contadores de datos.
        """
        context = super(Dashboard, self).get_context_data(*args, **kwargs)

        # Contamos la cantidad de cada elemento de la base de datos
        # para reportarlo en el Dashboard
        context['profesores'] = Profesor.objects.all().count()
        context['asignaturas'] = Asignatura.objects.all().count()
        context['departamento'] = Departamento.objects.all().count()

        return context
