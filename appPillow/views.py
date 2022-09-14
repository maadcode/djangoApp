from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from .services import negativo, umbral, invumbral, biumbral, invbiumbral, escala_gris, invescala_gris, extension, nivelgrises

# Create your views here.
def index(request):
    title = 'Django App usando Pillow - Grupo 8'
    return render(request, 'index.html', {
        'title': title
    })

def negativoView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = negativo(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def umbralView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = umbral(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def invumbralView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = invumbral(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def biumbralView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = biumbral(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def invbiumbralView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = invbiumbral(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def escala_grisView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = escala_gris(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def invescala_grisView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = invescala_gris(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def extensionView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = extension(imagenUrl)
    return JsonResponse(stringBase64, safe=False)

def nivelgrisesView(request):
    imagenUrl = 'C:\\Users\\Pc\\Documents\\Python Projects\\DjangoProject\\appPillow\\static\\images\\image.jpeg'
    stringBase64 = nivelgrises(imagenUrl)
    return JsonResponse(stringBase64, safe=False)
