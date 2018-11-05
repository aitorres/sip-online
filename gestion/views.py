from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')

class agregarProfesor(View):
    template_name = 'profesores/agregar.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse("Metodo Get")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Metodo Post")
      