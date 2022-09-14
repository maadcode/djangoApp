# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .services import inverso, umbral, invumbral, biumbral, invbiumbral, escala_gris, invescala_gris, extension

# Create your views here.
def index(request):
    title = 'Django App usando Pillow - Grupo 8'
    return render(request, 'index.html', {
        'title': title
    })