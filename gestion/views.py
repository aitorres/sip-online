from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from gestion.models import Profesor

class Dashboard(generic.TemplateView):
    """
    Controlador para el dashboard principal de la aplicación.
    Renderiza la plantilla de manera estática.
    """

    template_name = "dashboard.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args, **kwargs)
        context['profesores'] = Profesor.objects.all().count()
        #context['asignaturas'] = Asignatura.objects.all().count()
        #context['departamento'] = Departamento.objects.all().count()
        return context
