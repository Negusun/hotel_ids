from django.db import models
from django.contrib.auth.models import User

#pais model
class Pais(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

#cuidad model
class Ciudad(models.Model):
    nombre = models.CharField(max_length=250)
    pais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#hotel model
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
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#tipo habitacion model
class TipoHabitacion(models.Model):
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.descripcion

#habitacion model
class Habitacion(models.Model):
    numero = models.IntegerField()
    precio = models.IntegerField()
    capacidad = models.IntegerField()
    tipo_habitacion = models.ForeignKey(TipoHabitacion, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)

#Huesped model
class Huesped(models.Model):
    ci = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    nombre = models.CharField(max_length=60)
    apellido_pat = models.CharField(max_length=60)
    apellido_mat = models.CharField(max_length=60)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now=False)

    def __str__(self):
        return str(self.nombre)

#Acompanante model
class Acompanante(models.Model):
    ci = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellido_pat = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField(auto_now=False)
    huesped = models.ForeignKey(Huesped, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

#EstadoReserva model
class EstadoReserva(models.Model):
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return str(self.descripcion)

#Reserva model
class Reserva(models.Model):
    fecha_ingreso = models.DateField(auto_now=False)
    fecha_salida = models.DateField(auto_now=False)
    huesped = models.ForeignKey(Huesped, null=True, blank=True, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoReserva, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.huesped)
