from django.urls import path
from.views import listaDeGrupos

urlpatterns = [
    path('grupos', listaDeGrupos)
]
