from django.urls import path
# Import das views criadas em views.py
from.views       import Grupos, excluirGrupo, excluirArtista, excluirComeback, visualizarComeback, visualizarArtista, visualizarGrupo, listaDeArtistas, listaDeComebacks, criarGrupo, criarArtista, criarComeback, editarArtista, editarGrupo, editarComeback, index

urlpatterns = [
    # A url /grupos vai chamar a view Grupos da views.py, que por sua vez, vai renderizar a página Grupos.html
    path('', Grupos, name="Grupos"),
    path('grupos', Grupos, name="Grupos"),
    path('artistas', listaDeArtistas, name="listaDeArtistas"),
    path('comebacks', listaDeComebacks, name="listaDeComebacks"), 
    path('criarGrupo', criarGrupo),
    path('criarArtista/<int:id>', criarArtista),
    path('criarComeback/<int:id>', criarComeback),
    path('editarGrupo/<int:id>', editarGrupo),
    path('editarArtista/<int:id>', editarArtista),
    path('editarComeback/<int:id>', editarComeback),
    path('visualizarGrupo/<int:id>', visualizarGrupo),
    path('visualizarArtista/<int:id>', visualizarArtista),
    path('visualizarComeback/<int:id>', visualizarComeback),
    path('excluirGrupo/<int:id>', excluirGrupo),
    path('excluirArtista/<int:id>', excluirArtista),
    path('excluirComeback/<int:id>', excluirComeback)
]
