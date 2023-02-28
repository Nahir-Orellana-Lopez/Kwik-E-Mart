from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from compras.forms import ClienteFormulario, ArticuloFormulario, ItemFormulario
from .models import Cliente, Articulo, ItemCarrito


def inicio(request):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)

def clientes(request):
    miFormulario = ClienteFormulario()
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'],  
                            email=informacion['email'],
                            habilitado=informacion['habilitado'])
            cliente.save()
            return HttpResponseRedirect("/compras/clientes")
             
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes, "miFormulario":miFormulario}
    plantilla = loader.get_template("clientes.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

def eliminarCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return HttpResponseRedirect('/compras/clientes')

def articulos(request):
    miFormulario = ArticuloFormulario()
    if request.method == 'POST':
        miFormulario = ArticuloFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulo(nombre=informacion['nombre'],  
                            categoria=informacion['categoria'],
                            marca=informacion["marca"],
                            precio_unitario=informacion['precio_unitario'],
                            stock=informacion["stock"],
                            disponible=informacion["disponible"])
            articulo.save()
            return HttpResponseRedirect("/compras/articulos")
             
    articulos = Articulo.objects.all().order_by('categoria').values()
    contexto = {"articulos": articulos, "miFormulario": miFormulario}
    plantilla = loader.get_template("articulos.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

def editarArticulo(request, articulo_id):
    miFormulario = ArticuloFormulario()
    if request.method == 'POST':
        miFormulario = ArticuloFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            articulo = Articulo(id=articulo_id,
                            nombre=informacion['nombre'],  
                            categoria=informacion['categoria'],
                            marca=informacion["marca"],
                            precio_unitario=informacion['precio_unitario'],
                            stock=informacion["stock"],
                            disponible=informacion["disponible"])
            articulo.save()
            return HttpResponseRedirect("/compras/articulos/"+articulo_id)
             
    articulo = Articulo.objects.get(id=articulo_id)
    miFormulario = ArticuloFormulario(initial={"nombre":articulo.nombre, 
                                               "categoria": articulo.categoria, 
                                               "marca": articulo.marca,
                                               "precio_unitario": articulo.precio_unitario,
                                               "stock": articulo.stock,
                                               "disponible": articulo.disponible
    })
    contexto = {"articulo": articulo, "miFormulario": miFormulario}
    plantilla = loader.get_template("editarArticulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

def eliminarArticulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    articulo.delete()
    return HttpResponseRedirect('/compras/articulos')

def verArticulo(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    contexto = {"articulo": articulo}
    plantilla = loader.get_template("articulo.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

def carrito(request, cliente_id):     
    carrito = ItemCarrito.objects.all().filter(cliente_id=cliente_id)
    for i in carrito:
        i.suma_parcial = i.articulo.precio_unitario * i.cantidad
    cliente = Cliente.objects.get(pk=cliente_id)
    contexto = {"cliente": cliente,"carrito": carrito}
    plantilla = loader.get_template("carrito.html")
    documento = plantilla.render(contexto,request)
    return HttpResponse(documento)

def eliminarItem(request, item_id, cliente_id):
    item = ItemCarrito.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/compras/carrito/'+cliente_id)

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
    categoria = request.GET.get('categoria', '')
    nombre = request.GET.get('nombre', '')
    marca = request.GET.get('marca', '')
    articulos = Articulo.objects.filter(categoria__icontains=categoria,
                                        nombre__icontains=nombre,
                                        marca__icontains=marca)
    return render(request, "buscar.html", {"cliente":cliente, "articulos":articulos,
                                           "categoria":categoria, "nombre":nombre, "marca":marca})
    
def acercaDeMi(request):
    plantilla = loader.get_template("acercaDeMi.html")
    documento = plantilla.render({},request)
    return HttpResponse(documento)
   
# miFormulario = ItemFormulario()
# if request.method == 'POST':
#     miFormulario = ItemFormulario(request.POST)
    
#     if miFormulario.is_valid():
#         informacion = miFormulario.cleaned_data
#         item = ItemCarrito(cantidad=informacion['cantidad'],
#                         articulo=Articulo(id=1),
#                         cliente=Cliente(id=cliente_id))
#         item.save()
#         return HttpResponseRedirect("/compras/carrito/"+cliente_id)
