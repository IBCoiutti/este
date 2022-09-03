from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    fecha_nacimiento=models.DateField()
    residencia=models.CharField(max_length=50)
    email=models.EmailField()
    





