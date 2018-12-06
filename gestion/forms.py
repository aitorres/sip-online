# encoding=utf-8

"""
Módulo que incluye los formularios requeridos para la gestión
de la inscripción de postgrado.
"""

from django import forms

from gestion.models import Asignatura, Profesor, Departamento

class AgregarOfertaTrimestralPaso1(forms.Form):

    trimestre = forms.ChoiceField(
        choices=(
            ("EM", "Enero - Marzo"),
            ("AJ", "Abril - Julio"),
            ("JA", "Julio - Agosto"),
            ("SD", "Septiembre - Diciembre"),
        )
    )

    ano = forms.IntegerField(
        min_value=1967,
        max_value=2200
    )

    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all()
    )

    asignaturas = forms.ModelMultipleChoiceField(
        queryset=Asignatura.objects.all()
    )

class AgregarOfertaTrimestralPaso2(forms.Form):

     def __init__(self, *args, **kwargs):
        super(AgregarOfertaTrimestralPaso2, self).__init__(*args, **kwargs)
        cantidad = Asignatura.objects.all().count()
        for i in range(cantidad):
            id_asignatura = i+1
            self.fields['profesores_%d' % id_asignatura] = forms.ModelMultipleChoiceField(
                queryset=Profesor.objects.filter(asignaturas__id__contains=id_asignatura),
                required=False
            )