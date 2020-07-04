from django.urls import path
# Import das views criadas em views.py
from.views       import listaDeGrupos, listaDeArtista, listaDeComebacks, criarGrupo, criarArtista, criarComeback, editarArtista, editarGrupo, editarComeback, index

urlpatterns = [
    # A url /grupos vai chamar a view listaDeGrupos da views.py, que por sua vez, vai renderizar a página listaDeGrupos.html
    path('', listaDeGrupos, name="listaDeGrupos"),
    path('grupos', listaDeGrupos, name="listaDeGrupos"),
    path('artistas', listaDeArtista, name="listaDeArtistas"),
    path('comebacks', listaDeComebacks, name="listaDeComebacks"), 
    path('criarGrupo', criarGrupo),
    path('criarArtista', criarArtista),
    path('criarComeback', criarComeback),
    path('editarGrupo/<int:id>', editarGrupo),
    path('editarArtista/<int:id>', editarArtista),
    path('editarComeback/<int:id>', editarComeback)
]
