from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')


class AgregarProfesor(CreateView):
    template_name = 'profesores/agregar.html'
    model = Profesor
    fields = '__all__' 