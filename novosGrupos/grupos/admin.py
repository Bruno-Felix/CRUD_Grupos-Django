from django.contrib import admin
# Import das models criadas no models.py
from .models        import Grupo, Comeback, Artista

# Register your models here.

class GrupoAdmin(admin.ModelAdmin):
    # List_display vai mostrar infos desejadas na url /admin/grupos/grupo/, já padrão do admin
    list_display = ('nome', 'debut', 'resumo')

class ArtistaAdmin(admin.ModelAdmin):
    # List_display vai mostrar infos desejadas na url /admin/grupos/artista/, já padrão do admin
    list_display = ('nome', 'grupo')

class ComebackAdmin(admin.ModelAdmin):
    # List_display vai mostrar infos desejadas na url /admin/grupos/comeback/, já padrão do admin
    list_display = ('nome', 'grupo', 'data', 'views')

# Registar vai habilitar o trabalho com as classes e suas funções, 
# Nesse caso da Model(ex.: class Grupo) para trabalho com a model como todo: GET, SET, POST, DELETE e a
# ModelAdmin(ex.: class GrupoAdmin) para visualização de informações desejadas da model no admin.
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Comeback, ComebackAdmin)