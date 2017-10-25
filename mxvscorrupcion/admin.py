from django.contrib import admin
from .models import Sectores, Paises, Empresa, Cuestionario, Pregunta, Articulo, Catalogo_Preguntas

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Sectores)
admin.site.register(Paises)
admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Articulo)
admin.site.register(Catalogo_Preguntas)