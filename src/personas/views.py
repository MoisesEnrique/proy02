from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy

#importamos los modelos de persona
from .models import Persona

#importamos el formulario que creamos
from .forms import PersonaForm

#importamos el nuevo formulario plano que creamos
from .forms import RawPersonaForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView, 
    DeleteView,

    View,
)

from django.urls import reverse

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
    #definimos los campos iniciales del formulario para nombres y edad
    initialValues = {
        'nombres':'Sin Nombre',
        'edad':'25'
    }

    obj = Persona.objects.get(id=2) #Creamos una variable que guarde los datos de una persona, en este caso con id = 2
    form = PersonaForm(request.POST or None, instance=obj, initial=initialValues) #le enviamos la instancia del objeto con clave 2
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

#definimos la clase para el formulario plano
def personaAnotherCreateView(request):
    form = RawPersonaForm()     #request.GET
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   #funcion devuelve los datos limpios
            Persona.objects.create(**form.cleaned_data)      #persona objects accede a todos los objetos y create agrega uno. Enviamos la variable form.cleaned_data, pero debemos anteponer ** para que detecte como diciionario
        else:
            print(form.errors)      #muestra los errores

    context = {
        'form':form,
    }
    return render(request, 'personasCreate.html', context)

def personasShowObject(request, myID): #recibe el iD
    obj = get_object_or_404(Persona, id=myID)   #Linea que muestra un error contrlado si no eencuentra el id
    context = {
        'objeto':obj,
    }
    return render(request, "test.html", context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id=myID)

    if request.method == 'POST':
        print("lo borro")
        obj.delete()
        return redirect('../../')  #Retrocediendo 2 niveles en la urll para mostrar la lista de usuarios
    context = {
        'object':obj,
    }

    return render(request, 'deletePersona.html', context)

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList':queryset,
    }
    return render(request, 'showPersonas.html', context)


#Creamos una clase para la vista del ListView, tenemos que importarla de django.views.generic.list

class PersonaListView(ListView):
    model = Persona #el modelo trabaja con el modelo personas, la instancia provendra de aca
    queryset = Persona.objects.filter(edad__lte='45')   #consulta para mostrar los menores de 25

class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreateView(CreateView):
    model=Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador',
    ]

class PersonaUpdateView(UpdateView):
    model=Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador',
    ]

class PersonaDeleteView(DeleteView):
    model=Persona
    success_url = reverse_lazy('personas:persona-list')

class PersonaQueryView(View):
    def get(self, request, *args, **kwargs): #Definimos la funcion GET
        #return HttpResponse('<h1>Hola Mundo con clases</h1>')

        queryset = Persona.objects.filter(edad__lte='40')
        return JsonResponse(list(queryset.values()), safe=False)