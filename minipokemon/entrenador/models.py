from django.db import models

# Create your models here.
class entrenador(models.Model):
    nombre = models.CharField(max_length=30, default="nulo", blank=False)
    direccion = models.CharField(max_length=50, default="nulo", blank=False)
    correo = models.EmailField(max_length=30, default="nulo", blank=False, unique=True)
    telefono = models.CharField(max_length=10, default="nulo", blank=False)
    password = models.CharField(max_length=15, default="nulo", blank=False)