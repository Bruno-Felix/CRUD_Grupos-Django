from django.contrib import admin
from .models        import Grupo, Comeback, Artista

# Register your models here.

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'debut')

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo')

class ComebackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo', 'data', 'views')


admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Comeback, ComebackAdmin)