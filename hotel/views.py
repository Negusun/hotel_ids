from django.shortcuts import render
from hotel.models import Habitacion, Ciudad, Pais, Hotel, Reserva
from django.core.exceptions import *

from datetime import date, datetime
from django.http import HttpResponse
from django.core import serializers
import json

# Reserva
def reservar(request, id):
    try:
        habitacion = Habitacion.objects.get(id=id)
        if(False):
            info = 'Habitacion reservada gracias por preferirnos'
        else:
            info = None
    except:
        habitacion = None
        info = None

    context = {
        'habitacion': habitacion,
        'info': info
    }
    return render(request, 'habitacion/reservar.html', context)

# Buscador
def buscar(request):
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    ciudad = request.GET.get('ciudad')
    fechas = request.GET.get('fechas')

    # definir fecha actual para ser usadas en caso que no llegue una por parametro
    f_entrada = date.today()
    f_salida = date.today()

    # seleccionar todas las habitaciones a las que se les aplicaran filtros
    habitaciones = Habitacion.objects.all()

    # si llegan fechas por parametro formatearlas
    if fechas:
        fechas = fechas.split(' - ')
        f_entrada = datetime.strptime(fechas[0], "%Y/%m/%d").date()
        f_salida = datetime.strptime(fechas[1], "%Y/%m/%d").date()

    # validar que siempre hayan filtros de precios
    if not precio_min:
        precio_min = 10000
    if not precio_max:
        precio_max = 100000

    # aplicar filtros a habitaciones segun ciudad
    if ciudad:
        hoteles_id = Hotel.objects.filter(ciudad=ciudad)
        habitaciones = habitaciones.filter(hotel__in=hoteles_id).filter(precio__range=(precio_min, precio_max)).order_by('precio')
    if not ciudad:
        habitaciones = habitaciones.filter(precio__range=(precio_min, precio_max)).order_by('precio')

    # filtro para excluir habitaciones por rango de fechas reservadas
    habitaciones_id = Reserva.objects.filter(fecha_ingreso__range=[f_entrada, f_salida]).filter(fecha_salida__range=[f_entrada, f_salida])
    habitaciones = habitaciones.exclude(reserva__in=habitaciones_id)

    # ciudades disponibles
    ciudades = Ciudad.objects.all()

    context = {
        'title' : 'Habitaciones',
        'habitaciones' : habitaciones,
        'precio_min': precio_min,
        'precio_max': precio_max,
        'ciudades': ciudades
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
