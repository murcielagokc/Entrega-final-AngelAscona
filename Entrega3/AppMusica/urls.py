from django.contrib import admin
from django.urls import path
from AppMusica.views import * 
urlpatterns = [
    path("todos_album/", Mostrar_Album),
    path("nuevoalbum/", Agregar_album),
    path("BuscarAlbum/", buscarAlbum),
    path("ResultadosAlbum/",ResultadosBusqueda_Album),
    path("nuevoArtista/",Agregar_Artista),
    path("buscarArtista/", Agregar_Artista),
    path("ResultadoArtista/", ResultadosBusqueda_Artista),
    path("nuevoCancion/", Agregar_Cancion),
    path("BuscarCancion/", buscarCancion),
    path("ResultadosBusqueda_Cancion", ResultadosBusqueda_Cancion),
]
