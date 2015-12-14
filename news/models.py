from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField("Nombre de la categoria", max_length=100)
    slug = models.SlugField('Slug', unique=True, max_length=100)
    icon = models.ImageField('Icono de la categoria', upload_to='icons', blank=True)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.name

class News(models.Model):
    title  = models.CharField("Titulo", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True)
    text = models.TextField(verbose_name="Contenido")
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    posted_date = models.DateTimeField('Fecha creacion', auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __unicode__(self):
        return self.title


# Create your models here.
