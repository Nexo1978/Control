from django import forms
from AppControl.models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class VentaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"