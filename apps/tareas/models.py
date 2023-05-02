from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# Prioridades
class Prioridad(models.Model):
    nombre = models.TextField(verbose_name='Nombre', unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'prioridades'
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'
        ordering = ['nombre']

# Tareas
class Tarea(models.Model):
    nombre = models.TextField(verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    fecha_limite = models.DateField(verbose_name='Fecha Limite')
    terminada = models.BooleanField(default=False, verbose_name='Terminada')
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, verbose_name='Prioridad')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        return self.nombre + " " + self.descripcion + " - Fecha Límite: " + " " + " - Terminada: " + " "

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        db_table = 'tareas'
        ordering = ['fecha_limite']


