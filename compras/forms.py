from django import forms
from .models import Articulo, Mensaje

class CustomRadioSelect(forms.RadioSelect):
    option_template_name = 'compras/radio_option_custom.html'

ESCALA_CHOICES = (
    ("excelente.png", 'Excelente'),
    ("neutral.png", 'Neutral'),
    ("terrible.png", 'Terrible'),
)

opcionesCategoria = (
    ('bebidas','Bebidas'),
    ('alcohol','Alcohol'),
    ('embutidos', 'Embutidos'),
    ('azar','Azar'),
    ('juguetes','Juguetes'),
    ('almacen','Almacén'),
    ('golosinas','Golosinas'),
    ('limpieza','Limpieza'),
    ('congelados','Congelados'),
    ('desayuno','Desayuno'),
    ('panaderia','Panadería'),
    ('tabaco','Tabaco'),
    ('revistas','Revistas'),
    ('deportes','Deportes'),
    ('otro', 'Otro'),
    )

class ArticuloFormulario(forms.Form):
    categorias = forms.MultipleChoiceField(label='Categorías', widget=forms.CheckboxSelectMultiple, choices=opcionesCategoria)
    nombre = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    marca = forms.CharField(max_length=20, label='Marca', widget=forms.TextInput(attrs={'class':'form-control'}))
    precio_unitario = forms.FloatField(label='Precio Unitario', min_value=0, widget=forms.NumberInput(attrs={'class':'form-control', 'step': "0.1"}))
    stock = forms.IntegerField(label='Stock',min_value=0, widget=forms.NumberInput(attrs={'class':'form-control'}))
    disponible = forms.BooleanField(initial=True, required=False, label='Disponible', widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    imagen = forms.ImageField(required=False, label='Imagen', widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
       model = Articulo
       fields = ('categorias', 'nombre', 'marca', 'precio_unitario', 'stock', 'disponible', 'imagen')
    
class ItemFormulario(forms.Form):
    cantidad = forms.IntegerField()

class MensajeFormulario(forms.Form):
    mensaje = forms.CharField(required=False, max_length=200, label='Mensaje (Opcional)', widget=forms.Textarea(attrs={'class':'form-control', "rows":"2"}))
    escala_img = forms.ChoiceField(required=True, label='Escala de Krusty', widget=CustomRadioSelect(), choices = ESCALA_CHOICES)

    class Meta:
        model = Mensaje
        fields = ('mensaje', 'escala_img')

