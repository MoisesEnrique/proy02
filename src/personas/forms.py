from django import forms

#Para trabajar el modelo
from .models import Persona 


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador',
        ]

class RawPersonaForm(forms.Form):
    #definimos los campos
    nombres = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField(required=False)