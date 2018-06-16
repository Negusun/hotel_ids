from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reserva(models.Model):
    ESTADOS = (
        ('1', 'Disponible'),
        ('2', 'Reservada')
    )
    fecha_ingreso = models.DateTimeField(auto_now_add=False, auto_now=False)
    fecha_salida = models.DateTimeField(auto_now_add=False, auto_now=False)
    valor_reserva = models.IntegerField()
    estado_reserva = models.CharField(max_length=1, choices=ESTADOS, default=ESTADOS[0][0])
    habitacion = models.ForeignKey('habitacion.Habitacion', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return str(self.id)
