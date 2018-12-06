"""
Como agregar un URL

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""

from django.conf.urls import url, include
from django.contrib import admin
from gestion import views, forms

app_name = "gestion"

urlpatterns = [
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^profesores/$', views.ListarProfesores.as_view(), name='listar-profesores'),
    url(r'^profesores/agregar/$', views.AgregarProfesor.as_view(), name='agregar-profesor'),
    url(r'^profesores/editar/(?P<pk>[-\w]+)/$', views.EditarProfesor.as_view() , name='editar-profesor'),
    url(r'^profesores/eliminar/(?P<pk>[-\w]+)/$', views.EliminarProfesor.as_view() , name='eliminar-profesor'),
    url(r'^profesores/(?P<pk>[-\w]+)/$', views.VerProfesor.as_view(), name='ver-profesor'),
    url(r'^asignaturas/$', views.ListarAsignaturas.as_view(), name='listar-asignaturas'),
    url(r'^asignaturas/agregar/$', views.AgregarAsignatura.as_view(), name='agregar-asignatura'),
    url(r'^asignaturas/editar/(?P<pk>[-\w]+)/$', views.EditarAsignatura.as_view() , name='editar-asignatura'),
    url(r'^asignaturas/eliminar/(?P<pk>[-\w]+)/$', views.EliminarAsignatura.as_view() , name='eliminar-asignatura'),
    url(r'^asignaturas/(?P<pk>[-\w]+)/$', views.VerAsignatura.as_view(), name='ver-asignatura'),
    url(r'^ofertas/$', views.ListarOfertas.as_view(), name='listar-ofertas'),
    url(r'^ofertas/agregar/$', views.AgregarOferta.as_view([
        forms.AgregarOfertaTrimestralPaso1,
        forms.AgregarOfertaTrimestralPaso2
    ]), name='agregar-oferta'),
    url(r'^ofertas/eliminar/(?P<pk>[-\w]+)/$', views.EliminarOferta.as_view(), name='eliminar-oferta'),
    url(r'^ofertas/(?P<pk>[-\w]+)/$', views.VerOferta.as_view(), name='ver-oferta'),
    url(r'^ofertas-asignacion/$', views.ListarOfertasIncluyentes.as_view(), name='listar-ofertas-asignacion'),
    url(r'^ofertas-asignacion/actualizar/(?P<pk_oferta>[-\w]+)/$', views.actualizar_preferencias, name='actualizar-preferencias'),
    url(r'^ofertas-asignacion/(?P<pk>[-\w]+)/$', views.VerOfertaIncluyente.as_view(), name='ver-oferta-asignacion'),
]
