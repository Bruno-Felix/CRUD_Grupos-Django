from django.urls import path
# Import das views criadas em views.py
from.views       import listaDeGrupos, listaDeArtista, criarGrupo, index

urlpatterns = [
    # A url /grupos vai chamar a view listaDeGrupos da views.py, que por sua vez, vai renderizar a página listaDeGrupos.html
    path('', index),
    path('grupos', listaDeGrupos, name="listaDeGrupos"),
    path('artistas', listaDeArtista, name="listaDeArtista"), 
    path('criarGrupo', criarGrupo)
]
