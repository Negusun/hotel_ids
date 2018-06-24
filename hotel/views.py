from django.shortcuts import render
from hotel.models import Habitacion, Ciudad, Pais, Hotel

from django.http import HttpResponse
from django.core import serializers
import json

# Create your views here.
def buscar(request):
    precio_min = request.GET.get('precio_min') #diccionario
    precio_max = request.GET.get('precio_max') #diccionario

    if not precio_min:
        precio_min = 10000

    if not precio_max:
        precio_max = 100000

    habitaciones = Habitacion.objects.filter(precio__range=(precio_min, precio_max)).order_by('precio')

    context = {
        'title' : 'Habitaciones',
        'habitaciones' : habitaciones,
        'precio_min': precio_min,
        'precio_max': precio_max
    }
    return render(request, 'habitacion/listar.html', context)

# def inicio(request):
#     ciudades = Ciudad.objects.all()
#     paises = Pais.objects.all()
#     context = {
#         'title' : 'Inicio',
#         'ciudades' : ciudades,
#         'paises' : paises
#     }
#     return render(request, 'inicio.html', context)

# def habitaciones(request):
#     habitaciones = Habitacion.objects.all().order_by('precio', 'hotel')
#     context = {
#         'title' : 'Habitaciones',
#         'habitaciones' : habitaciones
#     }
#     return render(request, 'habitacion/listar.html', context)
