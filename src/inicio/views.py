from django.shortcuts import render

#importamos la libreria HTTPResponse de Django
from django.http import HttpResponse

# Create your views here.

#Definimos una funcion que va a hacer la interfaz(controlador) entre el modelo y el template
def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>Hola mundo desde DJango</h1>')