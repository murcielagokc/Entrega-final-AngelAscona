from django.db import models

# Create your models here.

class Album(models.Model):
    Nombre = models.CharField(max_length=50)
    Artista = models.CharField(max_length=50)
    Año = models.PositiveBigIntegerField()
    Genero = models.CharField(max_length=50)
    Disquera = models.CharField(max_length=50)

class Cancion(models.Model):
    Nombre = models.CharField (max_length=50)
    Artista= models.CharField (max_length=50)
    Genro= models.CharField (max_length=50)
    Album = models.CharField (max_length=50)

class Artista(models.Model):
    Nombre= models.CharField(max_length=50)
    Genero= models.CharField(max_length=50)
    Pais= models.CharField(max_length=30)


