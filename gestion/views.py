from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')

class EliminarProfesor(DeleteView):
    template_name = 'profesores/eliminar.html'
    model = Profesor
