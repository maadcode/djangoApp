from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('negativo/', views.negativoView),
    path('umbral/', views.umbralView),
    path('invumbral/', views.invumbralView),
    path('invbiumbral/', views.invbiumbralView),
    path('escala_gris/', views.escala_grisView),
    path('invescala_gris/', views.invescala_grisView),
    path('extension/', views.extensionView),
    path('nivelgrises/', views.nivelgrisesView),
]