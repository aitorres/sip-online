from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from gestion.models import Profesor, Asignatura, Departamento, Disponibilidad

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

    def get_context_data(self, **kwargs):
        """
        Permite agregar contenido adicional al diccionario genérico de
        contexto para pasar al template y que se renderice posteriormente.
        """

        # Obtenemos el diccionario de contexto por defecto
        context = super(VerProfesor, self).get_context_data(**kwargs)

        # Obtenemos los identificadores numéricos únicos de las disponibilidades
        # para saber qué campos mostrar como disponibles.
        lista_disponibilidades = []
        for disponibilidad in context['object'].disponibilidad.all():
            # Obtenemos el identificador único del dia/bloque en particular
            # y lo almacenamos en la lista
            identificador = disponibilidad.identificador_unico()
            lista_disponibilidades.append(identificador)

        # Agregamos los identificadores al diccionario de contexto
        context['lista_disponibilidades'] = lista_disponibilidades

        # Agregamos un diccionario con una manera sencilla de iterar para crear
        # la matriz de disponibilidades
        context['matriz_bloques'] = Disponibilidad.matriz_bloques()

        return context

class AgregarProfesor(generic.CreateView):
    """
    Controlador que maneja la lógica de agregar un profesor
    dado.
    """

    template_name = 'profesores/agregar.html'
    model = Profesor
    fields = '__all__'
    success_url = reverse_lazy('gestion:listar-profesores')

    def get_success_url(self):
        """
        En caso de que el agregar sea un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de profesores.
        """

        messages.success(self.request, 'El profesor ha sido agregado satisfactoriamente.')
        return super(AgregarProfesor, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de profesores.
        """

        messages.warning(self.request, 'Ocurrió un error al intentar agregar el profesor.')
        return redirect(self.success_url)

class EditarProfesor(generic.UpdateView):
    """
    Controlador que maneja la lógica y el formulario para
    modificar un profesor dado.
    """
    model = Profesor
    fields = '__all__'
    template_name = 'profesores/editar.html'
    success_url = reverse_lazy('gestion:listar-profesores')

    def get_success_url(self):
        """
        En caso de que el editar sea un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de profesores.
        """

        messages.success(self.request, 'El profesor ha sido modificado satisfactoriamente.')
        return super(EditarProfesor, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario de edicion se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de profesores.
        """

        messages.warning(self.request, 'Ocurrió un error al editar el profesor.')
        return redirect(self.success_url)


class EliminarProfesor(generic.DeleteView):
    """
    Controlador que maneja la lógica y el formulario paraProfe
    eliminar un profesor dado.
    """

    template_name = 'profesores/eliminar.html'
    model = Profesor
    success_url = reverse_lazy('gestion:listar-profesores')

    def get_success_url(self):
        """
        Si la eliminación del profesor es un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de profesores.
        """

        messages.success(self.request, 'El profesor ha sido eliminado satisfactoriamente.')
        return super(EliminarProfesor, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario para eliminar  se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de profesores.
        """

        messages.warning(self.request, 'Ocurrió un error al eliminar el profesor.')
        return redirect(self.success_url)

class ListarAsignaturas(generic.ListView):
    """
    Controlador que muestra una lista en tabla de todas las asignaturas.
    """
    template_name = 'asignaturas/listar.html'
    model = Asignatura
    context_object_name = "asignaturas"

class AgregarAsignatura(generic.CreateView):
    """
    Controlador que maneja la lógica de agregar una asignatura
    dada.
    """

    template_name = 'asignaturas/agregar.html'
    model = Asigantura
    fields = '__all__'
    success_url = reverse_lazy('gestion:listar-asignaturas')

    def get_success_url(self):
        """
        En caso de que el agregar sea un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.success(self.request, 'La asigantura ha sido agregado satisfactoriamente.')
        return super(AgregarAsignatura, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.warning(self.request, 'Ocurrió un error al intentar agregar una asignatura.')
        return redirect(self.success_url)

class EditarAsignatura(generic.UpdateView):
    """
    Controlador que maneja la lógica y el formulario para
    modificar una asigantura dada.
    """
    model = Asignatura
    fields = '__all__'
    template_name = 'asignaturas/editar.html'
    success_url = reverse_lazy('gestion:listar-asignaturas')

    def get_success_url(self):
        """
        En caso de que el editar sea un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.success(self.request, 'La asignatura ha sido modificado satisfactoriamente.')
        return super(EditarAsigantura, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario de edicion se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.warning(self.request, 'Ocurrió un error al editar la asignatura.')
        return redirect(self.success_url)
    
class EliminarAsignatura(generic.DeleteView):
    """
    Controlador que maneja la lógica y el formulario para
    eliminar una asignatura dada.
    """

    template_name = 'asignaturas/eliminar.html'
    model = Asignatura
    success_url = reverse_lazy('gestion:listar-asignaturas')

    def get_success_url(self):
        """
        Si la eliminación de la asignatura es un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.success(self.request, 'La asignatura ha sido eliminada satisfactoriamente.')
        return super(EliminarAsignatura, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario para eliminar  se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.warning(self.request, 'Ocurrió un error al eliminar la asignatura.')
        return redirect(self.success_url)

class VerAsignatura(generic.DetailView):
    """
    Controlador que permite visualizar los datos en detalle de una asignatura
    """

    template_name = 'asignaturas/ver.html'
    model = Asignatura
    context_object_name = "asignatura"
