from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Personas(models.Model):
    nombres = models.TextField()
    apellidos = models.TextField()
    edad = models.TextField()