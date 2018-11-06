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
        context['departamentos'] = Departamento.objects.all().count()

        return context

class ListarProfesores(generic.ListView):
    """
    Controlador que muestra una lista en tabla de todos los
    profesores.
    """
    template_name = 'profesores/listar.html'
    model = Profesor
    context_object_name = "profesores"

class VerProfesor(generic.DetailView):
    """
    Controlador que permite visualizar los datos en detalle de un profesor
    en particular.
    """

    template_name = 'profesores/ver.html'
    model = Profesor
    context_object_name = "profesor"

class AgregarProfesor(generic.CreateView):
    """
    Controlador que maneja la lógica de agregar un profesor
    dado.
    """

    template_name = 'profesores/agregar.html'
    model = Profesor
    fields = '__all__'

class EditarProfesor(generic.UpdateView):
    """
    Controlador que maneja la lógica y el formulario para
    modificar un profesor dado.
    """
    model = Profesor
    fields = '__all__'
    template_name = 'profesores/editar.html'

class EliminarProfesor(generic.DeleteView):
    """
    Controlador que maneja la lógica y el formulario para
    eliminar un profesor dado.
    """

    template_name = 'profesores/eliminar.html'
    model = Profesor
