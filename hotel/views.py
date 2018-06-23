from django.shortcuts import render
from hotel.models import Habitacion

# Create your views here.
def inicio(request):
    context = {
        'title' : 'Inicio',
    }
    return render(request, 'inicio.html', context)

def habitaciones(request):
    habitaciones = Habitacion.objects.all()
    context = {
        'title' : 'Habitaciones',
        'habitaciones' : habitaciones
    }
    return render(request, 'habitacion/listar.html', context)
