Django testing
1. Install Django and Channels:
●
 pip3 install django
●
 pip3 install channels==3.0.4
●
 pip3 install --upgrade pip
2. Create a new Django project:
●
 django-admin startproject django_app
●
 cd django_app
3. Create a new Django app:
●
 python manage.py startapp myapp
4. Create a basic view:
In myapp/views.py, add the following content:
from django.http import HttpResponse
def index(request):
return HttpResponse("Basic server startup!")
5. Configure URLs:
In django_app/urls.py, modify it to include the app’s URLs:
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('myapp.urls')),
]
6. App url:
Create a new file myapp/urls.py and add:
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
]
6. Update list of allowed hosts
● Open the settings.py file in your project directory (django_app/django_app/settings.py).
● Find the ALLOWED_HOSTS setting and update it like this:
● ALLOWED_HOSTS = ['192.168.100.123', 'localhost', '127.0.0.1']
7. Run the server:
python manage.py runserver 192.168.100.123:8000 ← this should be your PC’s IP address