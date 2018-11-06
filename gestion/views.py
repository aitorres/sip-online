from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')

class ListarProfesores(ListView):
    """
    Controlador que muestra una lista en tabla de todos los
    profesores.
    """
    template_name = 'profesores/listar.html'
    model = Profesor
    context_object_name = "profesores"
