from audioop import reverse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

class TareasListView(ListView):
    model = Tarea
    template_name = 'list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tareas'
        return context
