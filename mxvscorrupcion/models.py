from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.contrib.auth.models import User

class Corte(models.Model):
    # cuestionario = models.ForeignKey(Cuestionario)
    fecha_de_corte = models.DateTimeField(null=True)
    aprovado = models.NullBooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.fecha_de_corte)
# Create your models here.
class Glosario(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)

    class Meta:
        verbose_name = 'Glosario'
        verbose_name_plural = 'Glosarios'
        ordering = ['titulo']

    def __str__(self):
        return self.titulor

class Fuentes(models.Model):
    titulo = models.CharField(max_length=255)
    libro = models.CharField(max_length=255)
    url = models.URLField(max_length=500, blank=True, default='')

    class Meta:
        verbose_name = 'Fuente'
        verbose_name_plural = 'Fuentes'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

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
    id_reactivo = models.CharField(max_length=200)
    bloque = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)+ ' '+ self.id_reactivo + ' ' +self.descripcion
    class Meta:
        verbose_name = 'Catalogo_Preguntas'
        verbose_name_plural = 'Catalogo_Preguntas'

class Respuestas(models.Model):
    valor = models.CharField(max_length=3)
    opcion = models.CharField(max_length=200)
    def __str__(self):
        return self.opcion + ' ' + self.valor

class Pregunta(models.Model):
    reactivo = models.ForeignKey(Catalogo_Preguntas)
    respuesta = models.ForeignKey(Respuestas)
    def __str__(self):
        return 'Pregunta: %s || Respuesta: %s' %(self.reactivo, self.respuesta)

class Pregunta_temporal(models.Model):
    reactivo = models.ForeignKey(Catalogo_Preguntas)
    respuesta = models.ForeignKey(Respuestas)
    def __str__(self):
        return 'Pregunta: %s || Respuesta: %s' %(self.reactivo, self.respuesta)

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    sector = models.ForeignKey(Sectores)
    pais = models.ForeignKey(Paises)
    website_corporativo = models.URLField(max_length=1000)
    website_integridad = models.URLField(max_length=1000)
    # cuestionario = models.OneToOneField(Cuestionario)
    # corte =models.ForeignKey(Corte)
    tot100 = models.CharField(max_length=255, blank=True, null=True)
    tot = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre

class Cuestionario(models.Model):
    preguntas = models.ManyToManyField(Pregunta)
    created = models.DateTimeField(auto_now_add=True)
    Empresa = models.ForeignKey(Empresa)
    Corte = models.ForeignKey(Corte)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Pregunta: %s, created: %s, id %s' %(self.preguntas, self.created, str(self.pk))

class Articulo(models.Model):
    imagen = models.ImageField(upload_to='media/',null=True, blank=True)
    titulo = models.CharField(max_length=255)
    contenido = HTMLField()
    revista = HTMLField()
    autor = models.CharField(max_length=255)
    slug =models.SlugField(max_length=255, unique=True, null=True, blank=True)
    url = models.URLField(max_length=500, blank=True, default='')
    fecha = models.DateField(auto_now=False, auto_now_add=False)
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


class Entradas_Recientes(models.Model):
    titulo = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='media/',null=True, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    url = models.URLField(max_length=500, blank=True, default='')

    class Meta:
        verbose_name = "Entrada_Reciente"
        verbose_name_plural = "Entradas_Recientes"

    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', primary_key=True)
    telefono_fijo = models.CharField(max_length=12)
    telefono_celular = models.CharField(max_length=12)
    empresa = models.OneToOneField(Empresa, null=True)

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfiles'

    def __str__(self):
        return str(self.user.username)
