from django.contrib import admin
from .models import Sectores, Paises, Empresa, Cuestionario, Pregunta

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Sectores)
admin.site.register(Paises)
admin.site.register(Cuestionario)
admin.site.register(Pregunta)