from django.contrib import admin

from .models import Habitacion

# Register your models here.
from .models import Habitacion

class AdminHabitacion(admin.ModelAdmin):
    list_display = ['numero', 'precio', 'capacidad', 'tipo', 'hotel']
    list_filter = ['capacidad', 'precio', 'tipo']
    #list_editable = ['nombre', 'ubicacion', 'categoria']
    search_fields = ['numero']
    class Meta:
        model = Habitacion

admin.site.register(Habitacion, AdminHabitacion)

#admin.site.register(Habitacion)
