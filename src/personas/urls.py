from django.urls import path

from personas.views import personaTestView
from personas.views import personaCreateView
from personas.views import searchForHelp
from personas.views import personaAnotherCreateView
from personas.views import personasShowObject
from personas.views import personasDeleteView
from personas.views import personasListView


app_name = 'personas'
urlpatterns = [
    path('persona/', personaTestView, name="persona"),
    path('agregar/', personaCreateView, name="crear persona"),
    path('search/', searchForHelp, name="buscar"),
    path('anotherAdd/', personaAnotherCreateView, name="otro crear personas"),
    path('showPersonas/<int:myID>/', personasShowObject, name='ver_persona'), #recibe el parametro ID
    path('showPersonas/<int:myID>/delete/', personasDeleteView, name="eliminar persona"), #eliminar persona #utilizamos show persona pq ya recibe el id, lo ideal seria crear una nueva vista
    path('showPersonas/', personasListView, name="mostrar personas"),
]

