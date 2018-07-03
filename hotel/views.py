from django.shortcuts import render
from hotel.models import Habitacion, Ciudad, Pais, Hotel, Reserva, Huesped, EstadoReserva
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import *

from datetime import date, datetime

# # mis reservas
def getReservas(request):
    if(request.user.is_authenticated):
        id = request.user.id
        reservas = Reserva.objects.filter(user=id)
        context = {
            'reservas' : reservas,
            'title' : 'Mis Reservas'
        }
        return render(request, 'usuario/reservas.html', context)
    else:
        return HttpResponseRedirect(reverse('auth_login'))

def cancelarReserva(request):
    if(request.user.is_authenticated):
        id = request.user.id
        reservas = Reserva.objects.filter(user=id)
        context = {
            'reservas' : reservas,
            'title' : 'Mis Reservas'
        }
        return render(request, 'usuario/reservas.html', context)
    else:
        return HttpResponseRedirect(reverse('auth_login'))

# Reserva
def reservar(request, id):
    if(request.user.is_authenticated):
        try:
            habitacion = Habitacion.objects.get(id=id)
        except:
            habitacion = None

        context = {
            'habitacion': habitacion,
            'title': 'Reservando'
        }
        return render(request, 'habitacion/reservar.html', context)
    else:
        return HttpResponseRedirect(reverse('auth_login'))

def addReserva(request):
    if(request.user.is_authenticated):
        habitacion_id = request.POST.get('id')
        fechas = request.POST.get('fechas')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        ci = request.POST.get('ci')
        nombre = request.POST.get('nombre')
        apellido_pat = request.POST.get('apellido_pat')
        apellido_mat = request.POST.get('apellido_mat')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        user_id = request.POST.get('user_id');

        info = None

        if (habitacion_id or fecha_nacimiento or ci or nombre or apellido_pat or email or fechas or user_id):
            fechas = fechas.split(' - ')
            fecha_ingreso = datetime.strptime(fechas[0], "%Y/%m/%d").date()
            fecha_salida = datetime.strptime(fechas[1], "%Y/%m/%d").date()
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d").date()

            try:
                reservada = Reserva.objects.filter(
                        fecha_ingreso__range=[fecha_ingreso, fecha_salida]
                    ).filter(
                        fecha_salida__range=[fecha_ingreso, fecha_salida]
                    ).filter(
                        habitacion=habitacion_id
                    ).count()

                if reservada <= 0:
                    reserva = Reserva.objects.create(
                        fecha_ingreso = fecha_ingreso,
                        fecha_salida = fecha_salida,
                        huesped = Huesped.objects.create(
                            ci = ci,
                            email = email,
                            nombre = nombre,
                            apellido_pat = apellido_pat,
                            apellido_mat = apellido_mat,
                            telefono = telefono,
                            fecha_nacimiento = fecha_nacimiento
                        ),
                        habitacion = Habitacion.objects.get(id=habitacion_id),
                        estado = EstadoReserva.objects.get(descripcion='reservada'),
                        user = User.objects.get(id=user_id)
                    )
                    info = 'Reserva realizada con exito gracias.'
                else:
                    info = 'Esta habitacion esta reservada, prueba con una fecha diferente.'
            except ValueError:
                info = 'Error interno. '+ValueError
        else:
            info = 'No pudimos procesar tu reserva. \n Faltan datos.'

        return render(request, 'habitacion/res_reserva.html', {'info': info})
    else:
        return HttpResponseRedirect(reverse('auth_login'))

# Buscador
def buscar(request):
    if(request.user.is_authenticated):
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
    else:
        return HttpResponseRedirect(reverse('auth_login'))
