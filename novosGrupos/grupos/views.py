from django.shortcuts import render, redirect, get_object_or_404
# Import das models criadas no models.py
from .models          import Grupo, Artista, Comeback
from .forms           import GrupoForm, ArtistaForm, ComebackForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def Grupos(request):
    # Vai instanciar grupos para receber todos os objetos do tipo Grupo
    grupos = Grupo.objects.all().order_by('-id')

    # Vai retornar a renderização de um html Grupos.html
    return render(request, "grupos/grupos.html", {'grupos':grupos})

def listaDeArtistas(request):
    # Vai instanciar artistas para receber todos os objetos do tipo Artista
    artistas = Artista.objects.all().order_by('-id')

    # Vai retornar a renderização de um html listaDeArtistas.html
    return render(request, "grupos/listaDeArtistas.html", {'artistas':artistas})

def listaDeComebacks(request):
    # Vai instanciar comebacks para receber todos os objetos do tipo Comeback
    comebacks = Comeback.objects.all().order_by('-id')

    # Vai retornar a renderização de um html listaDeComebacks.html
    return render(request, "grupos/listaDeComebacks.html", {'comebacks':comebacks})


def criarGrupo(request):

    form = GrupoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = GrupoForm()
        return redirect('Grupos')
    else:
        form = GrupoForm()

    return render(request, "grupos/criarGrupo.html", {'form':form})

def criarArtista(request):

    form = ArtistaForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ArtistaForm()
        return redirect('listaDeArtistas')
    else:
        form = ArtistaForm()

    return render(request, "grupos/criarArtista.html", {'form':form})

def criarComeback(request):

    form = ComebackForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ComebackForm()
        return redirect('listaDeComebacks')
    else:
        form = ComebackForm()

    return render(request, "grupos/criarComeback.html", {'form':form})


def editarGrupo(request, id=None):

    grupo = get_object_or_404(Grupo, id=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = GrupoForm()
        return render(request, "grupos/visualizarGrupo.html", {'form':form, 'grupo':grupo})
    
    return render(request, "grupos/editarGrupo.html", {'form':form, 'grupo':grupo})

def editarArtista(request, id=None):

    artista = get_object_or_404(Artista, id=id)
    form = ArtistaForm(request.POST or None, instance=artista)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ArtistaForm()
        return render(request, "grupos/visualizarArtista.html", {'form':form, 'artista':artista})
    
    return render(request, "grupos/editarArtista.html", {'form':form, 'artista':artista})

def editarComeback(request, id=None):

    comeback = get_object_or_404(Comeback, id=id)
    form = ComebackForm(request.POST or None, instance=comeback)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ComebackForm()
        return render(request, "grupos/visualizarComeback.html", {'form':form, 'comeback':comeback})
    
    return render(request, "grupos/editarComeback.html", {'form':form, 'comeback':comeback})


def visualizarGrupo(request, id=None):

    grupo = get_object_or_404(Grupo, id=id)
    artistas = Artista.objects.all().order_by('-id')
    comebacks = Comeback.objects.all().order_by('-id')

    return render(request, "grupos/visualizarGrupo.html", {'grupo':grupo, 'artistas':artistas, 'comebacks':comebacks})

def visualizarArtista(request, id=None):

    artista = get_object_or_404(Artista, id=id)

    return render(request, "grupos/visualizarArtista.html", {'artista':artista})

def visualizarComeback(request, id=None):

    comeback = get_object_or_404(Comeback, id=id)

    return render(request, "grupos/visualizarComeback.html", {'comeback':comeback})
