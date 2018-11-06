from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import ListView
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')

class ListarProfesores(ListView):
	template_name = 'profesores/listar.html'
	model = Profesor