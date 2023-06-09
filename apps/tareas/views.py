from audioop import reverse
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from datetime import datetime, timedelta
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class TareasListView(ListView):
    model = Tarea
    template_name = 'listar.html'
    ordering = ['terminada', '-fecha_limite']

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            queryset = queryset.filter(fecha_limite__gte=start_date)
        
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            queryset = queryset.filter(fecha_limite__lte=end_date)
        
        queryset = queryset.filter(usuario=user)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tareas'
        context['start_date'] = self.request.GET.get('start_date')
        context['end_date'] = self.request.GET.get('end_date')
        return context

class TareaCreateView(SuccessMessageMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('tareas:tareas_listar')
    success_message = 'Tarea Creada'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Tarea'
        return context

class TareaUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('tareas:tareas_listar')
    success_message = 'Tarea Modificada'

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

class TareaDeleteView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar.html'
    success_url = reverse_lazy('tareas:tareas_listar')
    success_message = 'Tarea Eliminada'

    def test_func(self):
        tarea = self.get_object()
        return tarea.usuario == self.request.user

    def handle_no_permission(self):
        return redirect('tareas:tareas_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Tarea'
        return context

class TareaTerminarView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Tarea
    template_name = 'ver.html'
    fields = []
    success_url = reverse_lazy('tareas:tareas_listar')
    success_message = 'Tarea Terminada'

    def test_func(self):
        tarea = self.get_object()
        return tarea.usuario == self.request.user

    def handle_no_permission(self):
        return redirect('tareas:tareas_listar')

    def form_valid(self, form):
        tarea = form.save(commit=False)
        tarea.terminada = True
        tarea.save()
        return super().form_valid(form)