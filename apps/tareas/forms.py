from cProfile import label
from tkinter import Widget
from tokenize import Number
from django.forms import *
from .models import *

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'fecha_limite', 'prioridad']
        exclude = ['usuario']

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
