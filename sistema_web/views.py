from django.shortcuts import render, redirect, get_object_or_404

from .UserForm import UserForm
from .models import *


def ver_clientes(request):
    clientes = User.objects.all()
    if request.method == 'GET' and 'search' in request.GET:
        query = request.GET['search']
        clientes = User.objects.filter(nombre__icontains=query)
    return render(request, 'ver_clientes.html', {'clientes': clientes})


def agregar_cliente(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_activos')
    else:
        form = UserForm()

    return render(request, 'agregar_cliente.html', {'form': form})


def modificar_cliente(request, rut):
    cliente = get_object_or_404(User, rut=rut)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_activos')
    else:
        form = UserForm(instance=cliente)

    return render(request, 'modificar_cliente.html', {'form': form})


def ver_clientes_activos(request):
    clientes_activos = User.objects.filter(estado='Activo')
    return render(request, 'ver_clientes.html', {'clientes': clientes_activos, 'titulo': 'Clientes Activos'})


def ver_clientes_inactivos(request):
    clientes_inactivos = User.objects.filter(estado='Inactivo')
    return render(request, 'ver_clientes.html', {'clientes': clientes_inactivos, 'titulo': 'Clientes Inactivos'})


def filtrar_por_sector(request):
    if request.method == 'POST':
        sector = request.POST.get('sector')
        clientes_filtrados = User.objects.filter(sector=sector)
        return render(request, 'ver_clientes.html',
                      {'clientes': clientes_filtrados, 'titulo': f'Clientes del sector {sector}'})
    else:
        return render(request, 'filtrar_por_sector.html')

def ver_lecturas(request):
    lecturas = Lectura.objects.all()
    if request.method == 'GET' and 'search' in request.GET:
        query = request.GET['search']
        lecturas = Lectura.objects.filter(codigo_lectura__icontains=query)
    return render(request, 'ver_lecturas.html', {'lecturas': lecturas})

def registrar_lectura(request):
    # Lógica para manejar el registro de lecturas, por ejemplo, guardar en la base de datos
    if request.method == 'POST':
        # Lógica para manejar la información del formulario si se envía por POST
        pass
    else:
        # Lógica para manejar el caso GET, mostrar el formulario por ejemplo
        pass
    return render(request, 'registrar_lectura.html', {})

def ver_pagos(request):
    pagos = Pago.objects.all()
    if request.method == 'GET' and 'search' in request.GET:
        query = request.GET['search']
        pagos = Pago.objects.filter(codigo_pago__icontains=query)
    return render(request, 'ver_pagos.html', {'pagos': pagos})

def registrar_pago(request):
    # Lógica para manejar el registro de pagos, por ejemplo, guardar en la base de datos
    if request.method == 'POST':
        # Lógica para manejar la información del formulario si se envía por POST
        pass
    else:
        # Lógica para manejar el caso GET, mostrar el formulario por ejemplo
        pass
    return render(request, 'registrar_pago.html', {})
