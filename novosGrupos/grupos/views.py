from django.shortcuts import render
from .models import Grupo

# Create your views here.
def listaDeGrupos(request):
    grupos = Grupo.objects.all()
    return render(request, "grupos/listaDeGrupos.html", {'grupos':grupos})