from audioop import reverse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class TareasListView(ListView):
    model = Tarea
    template_name = 'list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tareas'
        return context

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'form.html'
    success_url = reverse_lazy('tareas:tareas_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        return context

