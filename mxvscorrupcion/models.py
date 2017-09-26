from django.db import models

# Create your models here.

class Sectores(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Paises(models.Model):
    pais = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['pais']

    def __str__(self):
        return self.pais

class Pregunta(models.Model):
    text_pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.text_pregunta


        
class Cuestionario(models.Model):
    preguntas = models.ManyToManyField(Pregunta)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Pregunta: %s, created: %s' %(self.preguntas, self.created)

        
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    sector = models.ForeignKey(Sectores)
    pais = models.ForeignKey(Paises)
    website_corporativo = models.URLField(max_length=255)
    website_integridad = models.URLField(max_length=1000)
    cuestionario = models.OneToOneField(Cuestionario)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre




