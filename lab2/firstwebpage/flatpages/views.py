from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # рендер index.html
    return render(request, 'index.html')

def static_handler(request):
    # рендер static_handler.html
    return render(request, 'static_handler.html')
