"""proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


#importamos la funcion myHomeView desde inicio/views.py
from inicio.views import myHomeView
from inicio.views import anotherView
from inicio.views import primeraView

urlpatterns = [
    path('admin/', admin.site.urls),
    #añadimos otro path vacio, para que llame la pagina de inicio
    path('', myHomeView, name="Pagina de Inicio"),
    path('another/', anotherView, name="Pagina Segunda"),
    path('primera/', primeraView, name="Pagina Primera"),
    #añadimos las urll de app personas aquipara q sean reconocidas
    path('personas/', include('personas.urls')),
]



