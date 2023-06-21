from cProfile import label
from tkinter import Widget
from tokenize import Number
from django.forms import *
from .models import *  
from django import forms
from django.utils import timezone
from datetime import date

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_limite', 'prioridad']
        exclude = ['usuario']

        error_messages = {
            'nombre': {
                'required': 'El campo Nombre es requerido.',
            },
            'descripcion': {
                'required': 'El campo Descripción es requerido.',
            },
            'fecha_limite': {
                'required': 'El campo Fecha Límite es requerido.',
            },
            'prioridad': {
                'required': 'El campo Prioridad es requerido.',
                'invalid_choice': 'Seleccionar una opción válida.'
            },
        }

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'fecha_limite': 'Fecha Límite',
            'prioridad': 'Prioridad'
        }
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'descripcion': Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'fecha_limite': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),

            'prioridad': Select(
                attrs={
                    'class': 'custom-select',
                }
            )

        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if ((len(nombre) < 5) or (len(nombre) > 100)):
            raise forms.ValidationError('El Nombre debe tener entre 5 y 100 caracteres.')
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if ((len(descripcion) < 5) or (len(descripcion) > 100)):
            raise forms.ValidationError('La Descripción debe tener al menos 5 caracteres.')
        return descripcion

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get('fecha_limite')
        formato_esperado = '%Y-%m-%d'
        fecha_actual = timezone.localdate()

        fecha_limite_str = fecha_limite.strftime(formato_esperado)
        if fecha_limite_str != self.data['fecha_limite']:
            raise forms.ValidationError('El formato de fecha es incorrecto.')

        if fecha_limite < fecha_actual:
            raise forms.ValidationError('La Fecha Límite debe ser mayor a la fecha actual.')
        return fecha_limite