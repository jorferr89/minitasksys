from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict

# Create your models here.

# Prioridades
class Prioridad(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'

# Tareas
class Tarea(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion')
    fecha_limite = models.DateField(default=date.today, verbose_name='Fecha Límite')
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE, verbose_name='Prioridad')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['prioridad'] = self.prioridad.toJSON()
        return item

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['fecha_limite']

    # Para convertir a MAYUSCULA
    def save(self, force_insert=False, force_update=False):
        self.titulo = self.titulo.upper()
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save(force_insert, force_update)


