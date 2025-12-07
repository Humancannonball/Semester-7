from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Django MQTT Server</h1><p>Server is running!</p>")

def websocket_test(request):
    return render(request, 'myapp/websocket_test.html')
