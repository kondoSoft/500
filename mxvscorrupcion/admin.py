from django.contrib import admin
from .models import Sectores, Paises, Empresa, Cuestionario, Pregunta, Articulo

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('empresa/css/admin.css',)
        }

# Register your models here.
admin.site.site_header = 'Las 500 vs la corrupción'
admin.site.register(Empresa)
admin.site.register(Sectores)
admin.site.register(Paises)
admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Articulo)
