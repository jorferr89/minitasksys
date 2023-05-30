from audioop import reverse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

# Create your views here.

class TareasListView(ListView):
    model = Tarea
    template_name = 'listar.html'
    ordering = ['-fecha_limite']
    
    def get_context_data(self, **kwargs):
        usuario = self.request.user
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tareas'
        context['object_list'] = Tarea.objects.filter(usuario=usuario)
        return context

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('tareas:tareas_listar')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        return context

class TareaUpdateView(UserPassesTestMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('tareas:tareas_listar')

    def test_func(self):
        tarea = self.get_object()
        return tarea.usuario == self.request.user

    def handle_no_permission(self):
        return redirect('tareas:tareas_listar')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Tarea'
        return context

class TareaDeleteView(UserPassesTestMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar.html'
    success_url = reverse_lazy('tareas:tareas_listar')

    def test_func(self):
        tarea = self.get_object()
        return tarea.usuario == self.request.user

    def handle_no_permission(self):
        return redirect('tareas:tareas_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Tarea'
        return context

class TareaTerminarView(UserPassesTestMixin, UpdateView):
    model = Tarea
    template_name = 'terminar.html'
    fields = ['terminada']
    success_url = reverse_lazy('tareas:tareas_listar')

    def test_func(self):
        tarea = self.get_object()
        return tarea.usuario == self.request.user

    def handle_no_permission(self):
        return redirect('tareas:tareas_listar')


