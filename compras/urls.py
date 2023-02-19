from django.urls import path
from compras import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes/', views.clientes, name="Clientes"),
    path('eliminarCliente/<cliente_id>', views.eliminarCliente, name="EliminarCliente"),
    path('articulos/', views.articulos, name="Articulos"),
    path('eliminarArticulo/<articulo_id>', views.eliminarArticulo, name="EliminarArticulo"),
    path('carrito/', views.carrito, name="Carrito"),
    path('eliminarItem/<item_id>', views.eliminarItem, name="EliminarItem")
]
