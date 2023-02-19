from django import forms
    
class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    habilitado = forms.BooleanField(initial=True, required=False)

class ArticuloFormulario(forms.Form):
    categoria = forms.CharField(max_length=200)
    nombre = forms.CharField(max_length=200)
    marca = forms.CharField(max_length=200)
    precio_unitario = forms.FloatField()
    stock = forms.IntegerField()
    disponible = forms.BooleanField(initial=True, required=False)

class ItemFormulario(forms.Form):
    cantidad = forms.IntegerField()