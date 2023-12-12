from django.shortcuts import render
from .models import User


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_activos')
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})


def modificar_cliente(request, rut):
    cliente = get_object_or_404(User, rut=rut)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_activos')
    else:
        form = ClienteForm(instance=cliente)

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
