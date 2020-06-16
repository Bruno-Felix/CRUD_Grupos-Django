from django.shortcuts import render
# Import das models criadas no models.py
from .models          import Grupo

# Create your views here.

def listaDeGrupos(request):
    # Vai instanciar grupos para receber todos os objetos do tipo Grupo
    grupos = Grupo.objects.all()

    # Vai retornar a renderização de um html listaDeGrupos.html
    return render(request, "grupos/listaDeGrupos.html", {'grupos':grupos})