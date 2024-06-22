from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    
class Docentes(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=150)
    materia = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre