from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from compras.forms import ArticuloFormulario, ItemFormulario
from .models import Articulo, ItemCarrito
from accounts.models import Avatar
from django.contrib.auth.decorators import login_required
from ast import literal_eval

def inicio(request):
    plantilla = loader.get_template("compras/inicio.html")
    avatares = Avatar.objects.filter(user=request.user.id)
    avatar = ""
    if(len(avatares) >= 1):
        avatar = avatares[0].imagen.name
    documento = plantilla.render({"avatar": avatar},request)
    return HttpResponse(documento)

# def clientes(request):
#     form = ClienteFormulario()
#     if request.method == 'POST':
#         form = ClienteFormulario(request.POST)
        
#         if form.is_valid():
#             informacion = form.cleaned_data
#             cliente = Cliente(nombre=informacion['nombre'],  
#                             email=informacion['email'],
#                             habilitado=informacion['habilitado'])
#             cliente.save()
#             return HttpResponseRedirect("/compras/clientes")
             
#     clientes = Cliente.objects.all()
#     contexto = {"clientes": clientes, "form":form}
#     plantilla = loader.get_template("compras/clientes.html")
#     documento = plantilla.render(contexto,request)
#     return HttpResponse(documento)

# def eliminarCliente(request, cliente_id):
#     cliente = Cliente.objects.get(id=cliente_id)
#     cliente.delete()
#     return HttpResponseRedirect('/compras/clientes')

def articulos(request):
    form = ArticuloFormulario()
    if request.method == 'POST':
        form = ArticuloFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            informacion = form.cleaned_data
            articulo = Articulo(nombre=informacion['nombre'],  
                            categorias=informacion['categorias'],
                            marca=informacion["marca"],
                            precio_unitario=informacion['precio_unitario'],
                            stock=informacion["stock"],
                            disponible=informacion["disponible"],
                            imagen=informacion["imagen"])
            articulo.save()
            return HttpResponseRedirect("/compras/articulos")
             
    articulos = Articulo.objects.all().order_by('categorias')
    # articulos = []
    contexto = {"articulos": articulos, "form": form}
    plantilla = loader.get_template("compras/articulos.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
def editarArticulo(request, articulo_id):
    form = ArticuloFormulario()
    if request.method == 'POST':
        form = ArticuloFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            informacion = form.cleaned_data
            articulo = Articulo(id=articulo_id,
                            nombre=informacion['nombre'],  
                            categorias=informacion['categorias'],
                            marca=informacion["marca"],
                            precio_unitario=informacion['precio_unitario'],
                            stock=informacion["stock"],
                            disponible=informacion["disponible"],
                            imagen=informacion["imagen"])
            
            fields_to_exclude = {}
            if(articulo.imagen == None):
                fields_to_exclude = {'imagen'}
            fields_to_update = [f.name for f in articulo._meta.get_fields() if f.name not in fields_to_exclude and not f.auto_created]
            articulo.save(update_fields=fields_to_update)
            # articulo.save()
            return HttpResponseRedirect("/compras/articulos/"+articulo_id)
             
    articulo = Articulo.objects.get(id=articulo_id)
    categorias = literal_eval(articulo.categorias)
    form = ArticuloFormulario(initial={"nombre":articulo.nombre, 
                                               "categorias": categorias, 
                                               "marca": articulo.marca,
                                               "precio_unitario": articulo.precio_unitario,
                                               "stock": articulo.stock,
                                               "disponible": articulo.disponible,
                                               "imagen": articulo.imagen
    })
    contexto = {"articulo": articulo, "form": form}
    plantilla = loader.get_template("compras/editarArticulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
def eliminarArticulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    articulo.delete()
    return HttpResponseRedirect('/compras/articulos')

def verArticulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    contexto = {"articulo": articulo}
    plantilla = loader.get_template("compras/articulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
def carrito(request, cliente_id):     
    carrito = ItemCarrito.objects.all().filter(cliente_id=cliente_id)
    for i in carrito:
        i.suma_parcial = i.articulo.precio_unitario * i.cantidad
    cliente = Cliente.objects.get(pk=cliente_id)
    contexto = {"cliente": cliente,"carrito": carrito}
    plantilla = loader.get_template("compras/carrito.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

@login_required
def eliminarItem(request, item_id, cliente_id):
    item = ItemCarrito.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/compras/carrito/'+cliente_id)

@login_required
def agregarItem(request, articulo_id, cliente_id):
    cantidad = request.POST.get('cantidad', 0)
    if(int(cantidad)>0):
        item = ItemCarrito(cantidad=cantidad,
                            articulo=Articulo(id=articulo_id),
                            cliente=Cliente(id=cliente_id))
        item.save()
    return HttpResponseRedirect('/compras/carrito/'+cliente_id)

def buscarArticulos(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    categorias = request.GET.get('categoria', '')
    nombre = request.GET.get('nombre', '')
    marca = request.GET.get('marca', '')
    articulos = Articulo.objects.filter(categoria__icontains=categorias,
                                        nombre__icontains=nombre,
                                        marca__icontains=marca)
    return render(request, "compras/buscar.html", {"cliente":cliente, "articulos":articulos,
                                           "categoria":categorias, "nombre":nombre, "marca":marca})

def acercaDeMi(request):
    plantilla = loader.get_template("compras/acercaDeMi.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)
   
# form = ItemFormulario()
# if request.method == 'POST':
#     form = ItemFormulario(request.POST)
    
#     if form.is_valid():
#         informacion = form.cleaned_data
#         item = ItemCarrito(cantidad=informacion['cantidad'],
#                         articulo=Articulo(id=1),
#                         cliente=Cliente(id=cliente_id))
#         item.save()
#         return HttpResponseRedirect("/compras/carrito/"+cliente_id)
