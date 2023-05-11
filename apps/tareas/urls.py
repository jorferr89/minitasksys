from django.urls import path
from apps.tareas.views import *

app_name = 'tareas'

urlpatterns = [
    path('tareas/', TareasListView.as_view(), name='tareas_lista'),
    path('tareas/crear/', TareaCreateView.as_view(), name='tareas_crear'),
]