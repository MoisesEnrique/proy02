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

    def clean_nombres(self, *args, **kwargs):
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('Primera letra en Mayuscula') 
    

class RawPersonaForm(forms.Form):
    #definimos los campos
    nombres = forms.CharField(label="Tu Nombre")
    apellidos = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder':'Ingrese un Apellido',
                'id':'apellidoID',
                'class':'special',
                'cold':'10',
            }
        )
    )		
    edad = forms.IntegerField(initial = 20, min_value=20, max_value=30)
    donador = forms.BooleanField(required=False)

    def clean_nombres(self, *args, **kwargs):
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('Primera letra en Mayuscula') 