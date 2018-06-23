from django.shortcuts import render
from hotel.models import Habitacion, Ciudad, Pais, Hotel

from django.http import HttpResponse
from django.core import serializers
import json

# Create your views here.
def buscar(request):
    nombre = request.GET.get('nombre') #diccionario
    hoteles = Hotel.objects.filter(nombre__startswith=nombre)
    hoteles = [ hotel_serializer(hotel) for hotel in hoteles ]

    return HttpResponse(json.dumps(hoteles), content_type='application/json')

def hotel_serializer(hotel):

    return {
        'nombre': hotel.nombre,
        'nombre': hotel.nombre,
        'ubicacion': hotel.ubicacion,
        'categoria': hotel.categoria
    }

def inicio(request):
    ciudades = Ciudad.objects.all()
    paises = Pais.objects.all()
    context = {
        'title' : 'Inicio',
        'ciudades' : ciudades,
        'paises' : paises
    }
    return render(request, 'inicio.html', context)

def habitaciones(request):
    habitaciones = Habitacion.objects.all().order_by('precio', 'hotel')
    context = {
        'title' : 'Habitaciones',
        'habitaciones' : habitaciones
    }
    return render(request, 'habitacion/listar.html', context)
