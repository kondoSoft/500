from django.db import models

# Create your models here.

class Sectores(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Paises(models.Model):
    pais = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['pais']

    def __str__(self):
        return self.pais

class Pregunta(models.Model):
    text_pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.text_pregunta


        
class Cuestionario(models.Model):
    preguntas = models.ForeignKey(Pregunta)
    respuesta = models.CharField(max_length=200)
    
    def __str__(self):
        return 'Pregunta: %s, respuesta: %s' %(self.preguntas, self.respuesta)

        
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    sector = models.ForeignKey(Sectores)
    pais = models.ForeignKey(Paises)
    website_corporativo = models.URLField(max_length=200)
    website_integridad = models.URLField(max_length=200)
    cuestionario = models.ManyToManyField(Cuestionario)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre




