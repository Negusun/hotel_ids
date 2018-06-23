from django.contrib import admin

# Register your models here.
from .models import Pais
from .models import Ciudad
from .models import Hotel
from .models import TipoHabitacion
from .models import Habitacion
from .models import Huesped
from .models import Acompanante
from .models import EstadoReserva
from .models import Reserva

admin.site.register([
        Hotel,
        TipoHabitacion,
        Habitacion,
        Huesped,
        Acompanante,
        EstadoReserva,
        Reserva
    ])
