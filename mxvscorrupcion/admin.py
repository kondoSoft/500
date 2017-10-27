from django.contrib import admin
from .models import Sectores, Paises, Empresa, Cuestionario, Pregunta, Articulo, Catalogo_Preguntas, Glosario, Fuentes

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('empresa/css/admin.css',)
        }

# Register your models here.
admin.site.site_header = 'Las 500 contra la corrupción'
admin.site.register(Empresa)
admin.site.register(Sectores)
admin.site.register(Paises)
admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Articulo)
admin.site.register(Catalogo_Preguntas)
admin.site.register(Glosario)
admin.site.register(Fuentes)
