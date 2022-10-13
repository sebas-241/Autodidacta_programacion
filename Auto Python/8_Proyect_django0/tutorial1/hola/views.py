from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hola(request):
    return render(request, 'hola/index.html')

def saludo(request, nombre):
    context = {'nombre': nombre}
    return render(request, 'hola/saludo.html', context)