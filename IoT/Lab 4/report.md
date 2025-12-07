# Lab 4: Django Testing

## Objective
Set up a basic Django web server with URL routing.

## Installation
```bash
pip install django channels==3.0.4
```

## Project Setup
```bash
django-admin startproject django_app
cd django_app
python manage.py startapp myapp
```

## Implementation

### myapp/views.py
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Basic server startup!")
```

### myapp/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### django_app/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### django_app/settings.py (modified)
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    ...
    'myapp',
]
```

## Running the Server
```bash
python manage.py runserver 127.0.0.1:8000
```

## Output
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 07, 2025 - 15:21:13
Django version 6.0, using settings 'django_app.settings'
Starting development server at http://127.0.0.1:8000/
```

### Testing with curl
```bash
$ curl http://127.0.0.1:8000/
Basic server startup!
```

## Conclusion
Django provides a robust framework for building web applications. The project demonstrates basic URL routing from the main project to an app, with a simple view returning an HTTP response.
