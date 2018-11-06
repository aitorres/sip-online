from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.http import HttpResponse
from gestion.models import Profesor 

def index(request):
    return render(request, 'template.html')

class EditarProfesor(UpdateView):
	model = Profesor
	fields = ['nombre','materias','Estatus','Disponibilidad']
	template_name_suffix = 'profesores/editar.html'
		