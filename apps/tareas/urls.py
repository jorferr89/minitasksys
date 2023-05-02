from django.urls import path
from apps.tareas.views import *

app_name = 'app.tareas'

urlpatterns = [
    path('tareas/', TareasListView.as_view(), name='tareas_list'),
]