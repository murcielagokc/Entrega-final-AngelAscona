from django import forms

class Album_Formulario(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Artista = forms.CharField(max_length=50)
    Año = forms.IntegerField()
    Genero = forms.CharField(max_length=50)
    Disquera = forms.CharField(max_length=50)

class Cancion_Formulario(forms.Form):
    Nombre = forms.CharField (max_length=50)
    Artista= forms.CharField (max_length=50)
    Genro= forms.CharField (max_length=50)
    Album = forms.CharField (max_length=50)

class Artista_Formulario(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Genero= forms.CharField(max_length=50)
    Pais= forms.CharField(max_length=30)