# MiniTaskSys

Módulo que simula la Gestión de Tarea (creación, modificación, eliminación, y finalización) con control de acceso.

## Instalación

1. Clonar o descargar el proyecto.
2. Crear un entorno virtual de python para instalar los requerimientos que se encuentran en el archivo requirements.txt.

```
$ python -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

3. Crear las migraciones y ejecutarlas.
```
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

4. Crear el usuario administrador.

```
(env) $ python manage.py createsuperuser
```

5. Ejecutar el servidor.

```
(env) $ python manage.py runserver
```

Ingresar desde: http://127.0.0.1:8000/

NOTA: La aplicación no tiene el CRUD de Prioridad, debe agregarlas desde el admin.
Usuario administrador http://127.0.0.1:8000/admin/