from django.shortcuts import render, redirect
# Import das models criadas no models.py
from .models          import Grupo, Artista
from .forms           import GrupoForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def listaDeGrupos(request):
    # Vai instanciar grupos para receber todos os objetos do tipo Grupo
    grupos = Grupo.objects.all().order_by('-id')

    # Vai retornar a renderização de um html listaDeGrupos.html
    return render(request, "grupos/listaDeGrupos.html", {'grupos':grupos})

def listaDeArtista(request):
    # Vai instanciar artistas para receber todos os objetos do tipo Artista
    artistas = Artista.objects.all().order_by('-id')

    # Vai retornar a renderização de um html listaDeArtistas.html
    return render(request, "grupos/listaDeArtistas.html", {'artistas':artistas})

def criarGrupo(request):

    form = GrupoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = GrupoForm()
        return redirect('listaDeGrupos')
    else:
        form = GrupoForm()

    return render(request, "grupos/criarGrupo.html", {'form':form})
