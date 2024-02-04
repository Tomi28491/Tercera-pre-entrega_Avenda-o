from django import forms  

class Crear_cuentaForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    contraseña = forms.IntegerField(required=True)

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    cantidad = forms.IntegerField(required=True)
    color = forms.CharField(max_length=50, required=True)
    precio = forms.FloatField(required=True)

class SucursalForm(forms.Form):
    direccion = forms.CharField(max_length=50, required=True)
    numero = forms.IntegerField(required=True)
    ciudad = forms.CharField(max_length=50, required=True)