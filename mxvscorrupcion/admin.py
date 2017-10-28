from django.contrib import admin

from .models import Sectores, Paises, Empresa, Cuestionario, Pregunta, Articulo, Catalogo_Preguntas, Glosario, Fuentes, Respuestas

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('empresa/css/admin.css',)
        }

# Register your models here.
admin.site.site_header = 'Las 500 contra la corrupción'


# admin.site.register(Empresa)
admin.site.register(Sectores)
admin.site.register(Paises)
# admin.site.register(Cuestionario)
admin.site.register(Pregunta)
admin.site.register(Articulo)
admin.site.register(Respuestas)
admin.site.register(Glosario)
admin.site.register(Fuentes)

class PreguntasInline(admin.TabularInline):
  model = Respuestas

class PreguntasAdmin(admin.ModelAdmin):
  inlines = [
    PreguntasInline
  ]

admin.site.register(Catalogo_Preguntas, PreguntasAdmin)

class CuestionarioInline(admin.TabularInline):
  model = Cuestionario

class CuestionarioAdmin(admin.ModelAdmin):
  inlines = [
    CuestionarioInline
  ]

admin.site.register(Empresa, CuestionarioAdmin)

class CuestionarioInline(admin.TabularInline):
  model = Cuestionario.preguntas.through

class CuestionarioAdmin(admin.ModelAdmin):
  inlines = [
    CuestionarioInline
  ]
  # exclude=('respuestas',)

admin.site.register(Cuestionario, CuestionarioAdmin)
