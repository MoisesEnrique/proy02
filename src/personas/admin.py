from django.contrib import admin

# Register your models here.

##importamos la clase persona definida en models
from .models import Persona

##dentro de admin reconozca la tabla persona	
admin.site.register(Persona)