from django.urls import path
from apps.tareas.views import *
from django.contrib.auth.decorators import login_required

app_name = 'tareas'

urlpatterns = [
    path('tareas/', login_required(TareasListView.as_view()), name='tareas_listar'),
    path('tareas/crear/', login_required(TareaCreateView.as_view()), name='tareas_crear'),
    path('editar/<int:pk>/', login_required(TareaUpdateView.as_view()), name='tareas_editar'),
    path('terminar/<int:pk>/', login_required(TareaTerminarView.as_view()), name='tareas_terminar'),
    path('eliminar/<int:pk>/', login_required(TareaDeleteView.as_view()), name='tareas_eliminar'),
]