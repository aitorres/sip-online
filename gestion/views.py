from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')

class VerProfesor(DetailView):
    """
    Permite visualizar los datos en detalle de un profesor
    en particular.
    """
    
    template_name = 'profesores/ver.html'
    model = Profesor
    context_object_name = "profesor"