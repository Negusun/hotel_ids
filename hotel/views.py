from django.shortcuts import render
from hotel.models import Habitacion, Ciudad, Pais, Hotel, Reserva
from django.core.exceptions import *

from datetime import date, datetime

# Reserva
def reservar(request, id):
    try:
        habitacion = Habitacion.objects.get(id=id)
    except:
        habitacion = None

    context = {
        'habitacion': habitacion,
        'title': 'Reservando'
    }
    return render(request, 'habitacion/reservar.html', context)

def addReserva(request):
    habitacion_id = request.POST.get('id')
    fechas = request.POST.get('fechas')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    ci = request.POST.get('ci')
    nombre = request.POST.get('nombre')
    apellido_pat = request.POST.get('apellido_pat')
    apellido_mat = request.POST.get('apellido_mat')
    telefono = request.POST.get('telefono')
    email = request.POST.get('email')

    info = None

    if (habitacion_id and fecha_nacimiento and ci and nombre and apellido_pat and email and fechas):
        fechas = fechas.split(' - ')
        fecha_ingreso = datetime.strptime(fechas[0], "%Y/%m/%d").date()
        fecha_salida = datetime.strptime(fechas[1], "%Y/%m/%d").date()
        info = 'Tu reserva se proceso revisa tu Email con los datos e instrucciones.'
    else:
        info = 'No pudimos procesar tu reserva. \n Intenta con otra fecha o una habitacion diferente.'

    return render(request, 'habitacion/res_reserva.html', {'info': info})

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
