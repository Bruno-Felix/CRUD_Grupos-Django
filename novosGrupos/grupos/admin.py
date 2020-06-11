from django.contrib import admin
from .models        import Grupo, Comeback, Integrante

# Register your models here.

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'debut')

class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo')

class ComebackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grupo', 'data', 'views')


admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(Comeback, ComebackAdmin)