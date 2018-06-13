from __future__ import unicode_literals

from django.db import models
from hotel.models import Hotel

# Create your models here.
class Habitacion(models.Model):
    TIPOS = (
        ('1', 'Sola'),
        ('2', 'Doble')
    )
    numero = models.IntegerField()
    precio = models.IntegerField()
    capacidad = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPOS, default=TIPOS[0][0])
    hotel = models.ForeignKey('hotel.Hotel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.numero
