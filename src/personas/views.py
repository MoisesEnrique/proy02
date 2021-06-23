from django.shortcuts import render

#importamos los modelos de persona
from .models import Persona

#importamos el formulario que creamos
from .forms import PersonaForm

# Create your views here.
# creamos la vista 
def personaTestView(request):
    obj = Persona.objects.get(id = 3)
    
    #definimos un diciionario para guardar los datos de la persona con id = 2
    context = {
        'nombre' : obj.nombres,
        'edad' : obj.edad,
    }
    return render(request, 'test.html', context)

#definimos una vista para el formulario
def personaCreateView(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid(): #Si todo esta completo lo grabe
        form.save()
        form = PersonaForm()  #Cargar de nuevo el formulario /blanquear los campos
    
    context = {
        'form': form,  #Le enviamos el formulario
    }

    return render(request, 'personasCreate.html', context)

#definimos la vista para search.html
def searchForHelp(request):
    return render(request, 'search.html', {})