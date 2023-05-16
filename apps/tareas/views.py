from audioop import reverse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class TareasListView(ListView):
    model = Tarea
    template_name = 'lista.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        # Obtén el usuario actual
        usuario = self.request.user

        # Filtra las tareas por el usuario actual
        queryset = Tarea.objects.filter(usuario=usuario)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tareas'
        return context

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('tareas:tareas_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        return context

class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('tareas:tareas_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Tarea'
        return context

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'eliminar.html'
    success_url = reverse_lazy('tareas:tareas_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Tarea'
        return context

class TareaTerminarView(UpdateView):
    model = Tarea
    fields = ['terminada']
    template_name = 'terminar.html'

    def get_success_url(self):
        return reverse_lazy('tareas:tareas_lista')

