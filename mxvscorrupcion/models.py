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
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    sector = models.ForeignKey(Sectores)
    pais = models.ForeignKey(Paises)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre