from django.contrib import admin

# Register your models here.
from .models import Reserva

class AdminReserva(admin.ModelAdmin):
    list_display = ['id', 'fecha_ingreso', 'fecha_salida', 'valor_reserva', 'estado_reserva', 'habitacion']
    #list_filter = ['categoria']
    #list_editable = ['nombre', 'ubicacion', 'categoria']
    #search_fields = ['nombre']
    class Meta:
        model = Reserva

admin.site.register(Reserva, AdminReserva)
