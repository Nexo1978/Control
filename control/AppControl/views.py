from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Proveedor, Venta
from .forms import *


# Create your views here.

def inicio(request):
    return render(request, 'AppControl/inicio.html')

def about(request):
    return render(request, 'AppControl/about.html')

def formulario_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('AppControl/inicio.html')
    else:
        formulario = ProductoForm()

    return render(request, 'AppControl/formproducto.html',{'formulario': formulario})

def formulario_proveedores(request):
    if request.method == 'POST':
        formulario2 = ProveedorForm(request.POST)
        if formulario2.is_valid():
            formulario2.save()
            return redirect('AppControl/inicio.html')
    else:
        formulario2 = ProveedorForm()

    return render(request, 'AppControl/formproveedor.html', {'formulario': formulario2})

def formulario_ventas(request):
    if request.method == 'POST':
        formulario3 = VentaForm(request.POST)
        if formulario3.is_valid():
            formulario3.save()
            return redirect('AppControl/inicio.html')
    else:
        formulario3 = VentaForm()

    return render(request, 'AppControl/formventas.html', {'formulario': formulario3})
