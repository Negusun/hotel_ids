"""app_hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy

from hotel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.buscar, name='buscar'),
    path('buscar', views.buscar, name='buscar'),
    path('reservar/<int:id>/', views.reservar, name='reservar'),
    path('cancelar/confirm', views.confirmCancel, name='confirmCancel'),
    path('cancelar/reserva', views.cancelReserva, name='cancelReserva'),
    path('reservas/', views.getReservas, name='getReservas'),
    path('reservar', views.addReserva, name='addReserva'),
    path('accounts/', include('registration.backends.default.urls'))
]
