from django.contrib import admin
from .models import Sectores, Paises, Empresa

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Sectores)
admin.site.register(Paises)