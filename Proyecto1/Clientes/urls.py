from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('crear_cuenta/', crear_cuenta, name="crear_cuenta"),
    path('agregar_productos/', agregar_productos, name="agregar_productos"),
    path('buscar/', buscar, name="buscar"),
    path('buscar_productos/', buscar_productos, name="buscar_productos"),
    path('productos/', productos, name="productos"),
    path('sucursal/', sucursal, name="sucursal"),
]