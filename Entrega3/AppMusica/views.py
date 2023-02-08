from django.shortcuts import render
from AppMusica.models import *
from AppMusica.forms import *
# Create your views here.

#Apartado de Album
def Mostrar_Album(request):
    todos_album= Album.objects.all()
    return render(request, "AppMusica/verAlbum.html",{"todos_album":todos_album})  

def Agregar_album(request):
    if request.method == "POST":
        miFormulario1= Album_Formulario(request.POST)
        print(miFormulario1)
        if miFormulario1.is_valid():
            informacion= miFormulario1.cleaned_data
            album= Album(Nombre=informacion["Nombre"], Artista=informacion["Artista"], Año=informacion["Año"], Genero=informacion["Genero"], Disquera=informacion["Disquera"])
            album.save()
            return render(request,"AppMusica/verAlbum.html")
    else:
        miFormulario1 = Album_Formulario()
    return render(request, "AppMusica/AlbumFormulario.html", {"miFormulario1":miFormulario1})

def buscarAlbum(request):
    return render(request, "AppMusica/BuscarAlbum.html")

def ResultadosBusqueda_Album(request):
    ArtistaBusqueda = request.GET["Artista"]
    ResultadosAlbum = Album.objects.filter(Artista_icontains=ArtistaBusqueda)
    return render(request, "AppMusica/ResultadosBA.html", {"info1":ArtistaBusqueda, "info2":ResultadosAlbum })

#Apartado de Artista

def Mostrar_Artista(request):
    todos_Artista=Artista.objects.all()
    return render(request, "AppMusica/verArtista.html",{"todos_Artista":todos_Artista})  

def Agregar_Artista(request):
    if request.method == "POST":
        Formulario2= Artista_Formulario(request.POST)
        print(Formulario2)
        if Formulario2.is_valid():
            informacion= Formulario2.cleaned_data
            artista = Artista(Nombre=informacion["Nombre"], Album=informacion["Album"], Año=informacion["Año"], Genero=informacion["Genero"], Disquera=informacion["Disquera"])
            artista.save()
            return render(request,"AppMusica/verArtista.html")
    else:
        Formulario2 = Artista_Formulario()
    return render(request, "AppMusica/ArtistaFormulario.html", {"Formulario2":Formulario2})

def buscarArtista(request):
    return render(request, "AppMusica/BuscarArtista.html")

def ResultadosBusqueda_Artista(request):
    AlbumBusqueda = request.GET["Album"]
    ResultadosArtista = Artista.objects.filter(Artista_icontains=AlbumBusqueda)
    return render(request, "AppMusica/ResultadosAT.html", {"info1":AlbumBusqueda, "info2":ResultadosArtista })

#Apartado de Canciones

def Mostrar_Canciones(request):
    todos_Canciones=Cancion.objects.all()
    return render(request, "AppMusica/verArCancion.html",{"todos_Cancion":todos_Canciones})  

def Agregar_Cancion(request):
    if request.method == "POST":
        Formulario3= Cancion_Formulario(request.POST)
        print(Formulario3)
        if Formulario3.is_valid():
            informacion= Formulario3.cleaned_data
            cancion = Cancion(Nombre=informacion["Nombre"], Album=informacion["Album"], Año=informacion["Año"], Genero=informacion["Genero"], Disquera=informacion["Disquera"], Artista=informacion["Artista"])
            cancion.save()
            return render(request,"AppMusica/verCancion.html")
    else:
        Formulario3 = Cancion_Formulario()
    return render(request, "AppMusica/CancionFormulario.html", {"Formulario3":Formulario3})

def buscarCancion(request):
    return render(request, "AppMusica/BuscarCancion.html")

def ResultadosBusqueda_Cancion(request):
    CancionBusqueda = request.GET["Cancion"]
    ResultadosCancion = Artista.objects.filter(Artista_icontains=CancionBusqueda)
    return render(request, "AppMusica/ResultadosAT.html", {"info1":CancionBusqueda, "info2":ResultadosCancion})