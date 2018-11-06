from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.http import HttpResponse
from gestion.models import Profesor 

def index(request):
    return render(request, 'template.html')

class EditarProfesor(UpdateView):
    model = Profesor
    fields = '__all__'
    template_name = 'profesores/editar.html'
        