from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hotel(models.Model):
    CATEGORIAS = (
        ('1', 'Economico'),
        ('2', 'Valor'),
        ('3', 'Calidad'),
        ('4', 'Superior'),
        ('5', 'Excepcional')
    )
    nombre = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=250, default='No proporcionada')
    categoria = models.CharField(max_length=1, choices=CATEGORIAS, default=CATEGORIAS[0][0])

    def __unicode__(self):
        return self.nombre
