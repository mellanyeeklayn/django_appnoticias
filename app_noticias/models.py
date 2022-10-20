from tabnanny import verbose
from django.db import models

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    titulo = models.CharField('título', max_length=128)
        
    conteudo = models.TextField('conteúdo')

    def __str__(self):
        return self.titulo    

# Create your models here.
