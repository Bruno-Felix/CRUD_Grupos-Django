from django.urls import path
# Import das views criadas em views.py
from.views       import listaDeGrupos

urlpatterns = [
    # A url /grupos vai chamar a view listaDeGrupos da views.py, que por sua vez, vai renderizar a página listaDeGrupos.html
    path('grupos', listaDeGrupos)
]
