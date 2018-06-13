from django.contrib import admin

# Register your models here.
from .models import Hotel

class AdminHotel(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ubicacion', 'categoria']
    list_filter = ['categoria']
    list_editable = ['nombre', 'ubicacion', 'categoria']
    search_fields = ['nombre']
    class Meta:
        model = Hotel

admin.site.register(Hotel, AdminHotel)
