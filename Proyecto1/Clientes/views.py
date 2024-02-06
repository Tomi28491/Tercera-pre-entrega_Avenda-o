from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "Clientes/home.html")


def crear_cuenta(request):
    if request.method == "POST":
        miForm = Crear_cuentaForm(request.POST)
        if miForm.is_valid():
            cuenta_nombre = miForm.cleaned_data.get("usuario")
            cuenta_mail = miForm.cleaned_data.get("email")
            cuenta_password = miForm.cleaned_data.get("contraseña")
            cuenta = Usuario(usuario=cuenta_nombre, email=cuenta_mail, password=cuenta_password)
            cuenta.save()
            return render(request, "Clientes/home.html")

    else:    
        miForm = Crear_cuentaForm()

    return render(request, "Clientes/crear_cuenta.html", {"form": miForm })

def agregar_productos(request):
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_cantidad = miForm.cleaned_data.get("cantidad")
            producto_color = miForm.cleaned_data.get("color")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Producto(nombre_producto=producto_nombre, cantidad=producto_cantidad, color=producto_color, precio=producto_precio)
            producto.save()
            return render(request, "Clientes/home.html")

    else:    
        miForm = ProductoForm()

    return render(request, "Clientes/agregar_producto.html", {"form": miForm })

def buscar(request):
    return render(request, "Clientes/buscar.html")

def buscar_productos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre_producto__icontains=patron)
        contexto = {"productos": productos }
        return render(request, "Clientes/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, "Clientes/productos.html", contexto)

def sucursal(request):
    if request.method == "POST":
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            sucursal_direccion = miForm.cleaned_data.get("direccion")
            sucursal_numero = miForm.cleaned_data.get("numero")
            sucursal_ciudad = miForm.cleaned_data.get("ciudad")
            sucursal = Sucursal(direccion=sucursal_direccion, numero=sucursal_numero, ciudad=sucursal_ciudad)
            sucursal.save()
            return render(request, "Clientes/home.html")

    else:    
        miForm = SucursalForm()

    return render(request, "Clientes/sucursal.html", {"form": miForm })