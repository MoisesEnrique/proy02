from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    donador = models.BooleanField()

    def get_absolute_url(self):
        return "/showPersonas/"+str(self.id)+"/" #cada vez que llamamaos a la funcion nos retorna la url:
                                                    # showPersonas/3/la funcion q se llame

