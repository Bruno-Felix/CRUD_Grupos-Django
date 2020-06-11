from django.contrib import admin
from .models        import Grupo, Comeback, Integrante
# Register your models here.

admin.site.register(Grupo)
admin.site.register(Integrante)
admin.site.register(Comeback)