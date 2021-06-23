from django.shortcuts import render

#importamos la libreria HTTPResponse de Django
from django.http import HttpResponse

# Create your views here.

#Definimos una funcion que va a hacer la interfaz(controlador) entre el modelo y el template
def myHomeView(request, *args, **kwargs):

    #definimos un  dicionario cualquiera
    myContext = {
        'myText' : "Esto es sobre nosotros",
        'myNumber' : 123,
        'myList' : [33, 54, 76, 87]
    }

    return render(request, "home.html", myContext)

def anotherView(request, *args, **kwargs):
    return HttpResponse('<h1>Hola mundo de otra Pagina</h1>')

def primeraView(request):
    return render(request, "primera.html", {})