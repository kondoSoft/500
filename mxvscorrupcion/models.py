from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from django.utils.text import slugify

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

class Catalogo_Preguntas(models.Model):
    descripcion = models.TextField()
    bloque = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Catalogo_Preguntas'
        verbose_name_plural = 'Catalogo_Preguntas'

class Pregunta(models.Model):
    reactivo = models.ForeignKey(Catalogo_Preguntas)
    respuesta = models.TextField(null=True)

    def __str__(self):
        return 'Pregunta: %s || Respuesta: %s' %(self.reactivo, self.respuesta)


class Cuestionario(models.Model):
    preguntas = models.ManyToManyField(Pregunta)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Pregunta: %s, created: %s' %(self.preguntas, self.created)

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    sector = models.ForeignKey(Sectores)
    pais = models.ForeignKey(Paises)
    website_corporativo = models.URLField(max_length=1000)
    website_integridad = models.URLField(max_length=1000)
    cuestionario = models.OneToOneField(Cuestionario)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = HTMLField()
    slug =models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        self.slug = slugify(self.titulo)
        #this line below save every fields of the model instance
        super(Articulo, self).save(*args, **kwargs)

        return self

    def get_absoulte_url(self):
        return reverse('articulos', args=[self.slug])

    def __str__(self):
        return self.titulo

class Corte(models.Model):
    cuestionario = models.ForeignKey(Cuestionario)
    fecha_de_corte = models.DateTimeField(null=True)
    aprovado = models.NullBooleanField(blank=True, null=True)
