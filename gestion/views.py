from django.contrib import messages
from django.core.mail import send_mail
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from gestion.forms import AgregarOfertaTrimestralPaso1

from gestion.models import (
    Profesor,
    Asignatura,
    Departamento,
    Disponibilidad,
    OfertaTrimestral,
    AsignacionProfesoral
)

def _enviar_correo(para, asunto, plantilla_mensaje, contexto):
    """
    Función privada para enviar un correo electrónico a los profesores
    según sea necesario.
    """

    mensaje = loader.render_to_string(
        plantilla_mensaje,
        contexto
    )

    return send_mail(
        asunto,
        mensaje,
        "SIP Online <no-reply@sip-online.com>",
        [para],
        fail_silently=False,
    )

class Dashboard(LoginRequiredMixin, generic.TemplateView):
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

class ListarProfesores(LoginRequiredMixin, generic.ListView):
    """
    Controlador que muestra una lista en tabla de todos los
    profesores.
    """
    template_name = 'profesores/listar.html'
    model = Profesor
    context_object_name = "profesores"

    def get_queryset(self):
        profesores = Profesor.objects.filter(
            departamento = self.request.user.profesor.departamento
        )
        return profesores

class VerProfesor(LoginRequiredMixin, generic.DetailView):
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

class AgregarProfesor(LoginRequiredMixin, generic.CreateView):
    """
    Controlador que maneja la lógica de agregar un profesor
    dado.
    """

    template_name = 'profesores/agregar.html'
    model = Profesor
    fields = (
        'nombre',
        'apellido',
        'cedula',
        'email',
        'disponibilidad',
        'departamento',
        'asignaturas'
    )
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

    def get_form(self):
        """
        Se modifica el método get_form para especificar restricciones en las opciones de algunos
        campos desplegables.
        """

        form = super(AgregarProfesor, self).get_form()
        form.fields['departamento'].queryset = Departamento.objects.filter(
            id = self.request.user.profesor.departamento.id
        )
        form.fields['asignaturas'].queryset = Asignatura.objects.filter(
            departamento = self.request.user.profesor.departamento
        )
        return form

class EditarProfesor(LoginRequiredMixin, generic.UpdateView):
    """
    Controlador que maneja la lógica y el formulario para
    modificar un profesor dado.
    """
    model = Profesor
    fields = (
        'nombre',
        'apellido',
        'cedula',
        'email',
        'disponibilidad',
        'departamento',
        'asignaturas'
    )
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
    
    def get_form(self):
        """
        Se modifica el método get_form para especificar restricciones en las opciones de algunos
        campos desplegables.
        """

        form = super(EditarProfesor, self).get_form()
        form.fields['departamento'].queryset = Departamento.objects.filter(
            id = self.request.user.profesor.departamento.id
        )
        form.fields['asignaturas'].queryset = Asignatura.objects.filter(
            departamento = self.request.user.profesor.departamento
        )
        return form

class EliminarProfesor(LoginRequiredMixin, generic.DeleteView):
    """
    Controlador que maneja la lógica y el formulario para
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

    def get_queryset(self):
        asignaturas = Asignatura.objects.filter(
            departamento = self.request.user.profesor.departamento
        )
        return asignaturas

class AgregarAsignatura(generic.CreateView):
    """
    Controlador que maneja la lógica de agregar una asignatura
    dada.
    """

    template_name = 'asignaturas/agregar.html'
    model = Asignatura
    fields = '__all__'
    success_url = reverse_lazy('gestion:listar-asignaturas')

    def get_success_url(self):
        """
        En caso de que el agregar sea un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.success(self.request, 'La asignatura ha sido agregado satisfactoriamente.')
        return super(AgregarAsignatura, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.warning(self.request, 'Ocurrió un error al intentar agregar una asignatura.')
        return redirect(self.success_url)

    def get_form(self):
        """
        Se modifica el método get_form para especificar restricciones en las opciones de algunos
        campos desplegables.
        """

        form = super(AgregarAsignatura, self).get_form()
        form.fields['departamento'].queryset = Departamento.objects.filter(
            id = self.request.user.profesor.departamento.id
        )
        return form

class EditarAsignatura(generic.UpdateView):
    """
    Controlador que maneja la lógica y el formulario para
    modificar una asignatura dada.
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
        return super(EditarAsignatura, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario de edicion se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de asignaturas.
        """

        messages.warning(self.request, 'Ocurrió un error al editar la asignatura.')
        return redirect(self.success_url)
    
    def get_form(self):
        """
        Se modifica el método get_form para especificar restricciones en las opciones de algunos
        campos desplegables.
        """

        form = super(EditarAsignatura, self).get_form()
        form.fields['departamento'].queryset = Departamento.objects.filter(
            id = self.request.user.profesor.departamento.id
        )
        return form

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

    def get_context_data(self, **kwargs):
        """
        Permite agregar contenido adicional al diccionario genérico de
        contexto para pasar al template y que se renderice posteriormente.
        """

        # Obtenemos el diccionario de contexto por defecto
        context = super(VerAsignatura, self).get_context_data(**kwargs)

        # Agregamos los identificadores al diccionario de contexto
        context['lista_disponibilidades'] = context['object'].horarios()

        # Agregamos un diccionario con una manera sencilla de iterar para crear
        # la matriz de disponibilidades
        context['matriz_bloques'] = Disponibilidad.matriz_bloques()

        return context

class ListarOfertas(generic.ListView):
    """
    Controlador que muestra una lista la oferta trimestral.
    """
    template_name = 'ofertas/listar.html'
    model = OfertaTrimestral
    context_object_name = "ofertas"

    def get_queryset(self):
        ofertas = OfertaTrimestral.objects.filter(
            departamento = self.request.user.profesor.departamento
        )
        return ofertas

class ListarOfertasIncluyentes(generic.ListView):
    """
    Controlador que muestra una lista las ofertas trimestrales en las que
    puedo marcar mi preferencia como profesor.
    """

    template_name = 'ofertas-asignacion/listar.html'
    model = OfertaTrimestral

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ofertas = OfertaTrimestral.objects.all()
        ofertas = [o for o in ofertas if not o.es_final]
        ofertas_importantes = []

        for oferta in ofertas:
            if self.request.user.profesor in oferta.profesores_ofertados():
                ofertas_importantes.append(oferta)

        context['ofertas'] = ofertas_importantes
        return context

class EliminarOferta(generic.DeleteView):
    """
    Controlador que maneja la lógica y el formulario para
    eliminar una oferta trimestral dada.
    """

    template_name = 'ofertas/eliminar.html'
    model = OfertaTrimestral
    success_url = reverse_lazy('gestion:listar-ofertas')

    def get_success_url(self):
        """
        Si la eliminación de la oferta trimestral es un éxito, muestra un mensaje de
        éxito utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de ofertas trimestrales.
        """

        messages.success(self.request, 'La oferta trimestral ha sido eliminada satisfactoriamente.')
        return super(EliminarOferta, self).get_success_url()

    def form_invalid(self, form):
        """
        En caso de que el formulario para eliminar  se reciba inválido, muestra un mensaje de
        error utilizando el framework de mensajes de Django y redirecciona a la URL
        de éxito, que en este caso es la lista de ofertas trimestrales.
        """

        messages.warning(self.request, 'Ocurrió un error al eliminar la oferta trimestral.')
        return redirect(self.success_url)

class AgregarOferta(SessionWizardView):
    """
    Controlador que maneja la lógica y el formulario para agregar una nueva
    oferta trimestral preliminar para un Departamento dado, en un formulario
    de dos pasos para asignar profesores junto con materias.
    """

    template_name = 'ofertas/agregar.html'

    def get_form(self, step=None, data=None, files=None):
        form = super(AgregarOferta, self).get_form(step, data, files)
        if type(form) == AgregarOfertaTrimestralPaso1:
            form.fields['departamento'].queryset = Departamento.objects.filter(
            id = self.request.user.profesor.departamento.id
            )
            form.fields['asignaturas'].queryset = Asignatura.objects.filter(
                departamento = self.request.user.profesor.departamento
            )
        return form

    def done(self, form_list, **kwargs):
        forms = list(form_list)
        paso1 = forms[0]
        paso2 = forms[1]

        trimestre = paso1['trimestre'].value()
        ano = paso1['ano'].value()[2:]
        departamento_id = paso1['departamento'].value()

        codigo_oferta = trimestre + ano
        departamento = Departamento.objects.get(pk=departamento_id)

        try:
            oferta = OfertaTrimestral.objects.create(
                trimestre=codigo_oferta,
                departamento=departamento
            )
        except IntegrityError:
            messages.warning(self.request, 'Ya existe una oferta trimestral para el trimestre y departamento escogidos.')
            return redirect('gestion:listar-ofertas')

        asignaturas = paso1['asignaturas'].value()

        emails_profesores = set()

        for asignatura_id in asignaturas:
            asignatura = Asignatura.objects.get(pk=asignatura_id)

            profesores = paso2['profesores_%s' % asignatura_id].value()
            for profesor_id in profesores:
                profesor = Profesor.objects.get(pk=profesor_id)

                AsignacionProfesoral.objects.create(
                    oferta_trimestral=oferta,
                    asignatura=asignatura,
                    profesor=profesor
                )

                emails_profesores.add(profesor.email)

        for email in emails_profesores:
            _enviar_correo(
                email,
                "[SIP ONLINE] Nueva oferta trimestral disponible",
                'emails/oferta_disponible.html',
                {
                    'oferta': oferta,
                }
            )

        messages.success(self.request, 'La oferta trimestral ha sido agregada satisfactoriamente.')
        return redirect('gestion:listar-ofertas')

    def get_context_data(self, form, **kwargs):
        context = super(AgregarOferta, self).get_context_data(form=form, **kwargs)

        if self.steps.current == '1':
            ids_asignaturas = set()
            for i in self.request.POST.getlist('0-asignaturas'):
                ids_asignaturas.add(i)
            nombres_asignaturas = dict()
            profesores_asignaturas = dict()
            for i in ids_asignaturas:
                asignatura = Asignatura.objects.get(pk=int(i))
                nombre = str(asignatura)
                nombres_asignaturas['1-profesores_%s' % i] = nombre
                profesores = asignatura.profesores()
                profesores_asignaturas['1-profesores_%s' % i] = profesores

            context.update(
                {
                    'ids_asignaturas': ids_asignaturas,
                    'nombres_asignaturas': nombres_asignaturas,
                    'profesores_asignaturas': profesores_asignaturas
                }
            )
        return context

class VerOferta(LoginRequiredMixin, generic.DetailView):
    """
    Controlador que permite visualizar los datos en detalle de una oferta
    trimestral en particular.
    """

    template_name = 'ofertas/ver.html'
    model = OfertaTrimestral
    context_object_name = "oferta"

    def get_context_data(self, **kwargs):
        """
        Permite agregar contenido adicional al diccionario genérico de
        contexto para pasar al template y que se renderice posteriormente.
        """

        # Obtenemos el diccionario de contexto por defecto
        context = super(VerOferta, self).get_context_data(**kwargs)

        # Obtenemos las asignaciones profesorales asignadas a esta oferta
        oferta = context['object']
        asignaciones = AsignacionProfesoral.objects.filter(
            oferta_trimestral=oferta
        )

        context['asignaciones'] = asignaciones

        return context

class VerOfertaIncluyente(LoginRequiredMixin, generic.DetailView):
    """
    Controlador que permite visualizar los datos en detalle de una oferta
    trimestral en particular.
    """

    template_name = 'ofertas-asignacion/ver.html'
    model = OfertaTrimestral
    context_object_name = "oferta"

    def get_context_data(self, **kwargs):
        """
        Permite agregar contenido adicional al diccionario genérico de
        contexto para pasar al template y que se renderice posteriormente.
        """

        # Obtenemos el diccionario de contexto por defecto
        context = super(VerOfertaIncluyente, self).get_context_data(**kwargs)

        # Obtenemos las asignaciones profesorales asignadas a esta oferta
        oferta = context['object']
        asignaciones = AsignacionProfesoral.objects.filter(
            oferta_trimestral=oferta,
            profesor=self.request.user.profesor
        )

        context['asignaciones'] = asignaciones

        return context

@login_required
def actualizar_preferencias(request, pk_oferta):
    template_name = 'ofertas-asignacion/actualizar.html'

    oferta = OfertaTrimestral.objects.get(pk=pk_oferta)
    asignaciones = AsignacionProfesoral.objects.filter(
        oferta_trimestral=oferta,
        profesor=request.user.profesor
    )

    if request.method == 'POST':
        for asignacion in asignaciones:
            try:
                marcado = request.POST['%s' % asignacion.id] == 'on'
            except MultiValueDictKeyError:
                marcado = False

            asignacion.es_preferida = marcado
            asignacion.save()

        messages.success(requedest, 'Preferencias actualizadas satisfactoriamente.')
        return redirect('gestion:listar-ofertas-asignacion')
    else:
        return render(
            request,
            template_name,
            {
                'asignaciones': asignaciones,
                'oferta': oferta
            }
        )

def buscar_oferta(request,periodo=None,ano=None):
    template_name = templates/ofertas/buscar.html
    if periodo == None or ano == None:
        return render(
            request,
            template_name
        )
    if periodo!=None:
        context = dict()
        ofertas = OfertaTrimestral.objects.filter(trimestre[:2]== periodo[:2])
        context['ofertas'] = ofertas
        return render(
            request,
            template_name,
            context
        )
        
    if periodo =='-' and ano!=None:
        context = dict()
        ofertas = OfertaTrimestral.objects.filter(trimestre[:1]=='-')
        context['ofertas'] = ofertas
        return render(
            request,
            template_name,
            context
        )
        
        
        
        