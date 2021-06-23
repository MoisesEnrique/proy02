from django.shortcuts import render

#importamos los modelos de persona
from .models import Persona

# Create your views here.
# creamos la vista 
def personaTestView(request):
    obj = Persona.objects.get(id = 2)
    
    #definimos un diciionario para guardar los datos de la persona con id = 2
    context = {
        'nombre' : obj.nombres,
        'edad' : obj.edad,
    }
    return render(request, 'personas/test.html', context)

