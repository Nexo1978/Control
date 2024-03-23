from django.urls import path
from AppControl.views import *
from AppControl.forms import *
from AppControl.models import *

urlpatterns = [
    path("", inicio, name= 'inicio'),
    path("about", about, name = 'about'),
    path("formproducto", ProductoForm, name='ingresoproducto'),
    path("formproveedores", ProveedorForm, name='ingresoproveedor' ),
    path("formventas", VentaForm, name='ingresoventas'),


]