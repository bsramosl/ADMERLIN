from django.urls import path
from PrincipalApp import views
from PrincipalApp.view.Category.views import *
from PrincipalApp.view.Client.views import *
from PrincipalApp.view.Product.views import *
from PrincipalApp.view.Sale.views import *
from PrincipalApp.view.DetSale.views import *
from django.contrib.auth.decorators import login_required

app_name = 'Merlin'
urlpatterns = [

   path('',views.Login.as_view(), name='Login'), 
   path('Logout',views.Logout.as_view(), name='Logout'), 
   path('Registro/',views.Registro.as_view(), name='Registro'),



   path('Inicio',views.Inicio.as_view(), name='Inicio'),  

   path('Venta/',views.Venta.as_view(), name='Venta'),  
 
  
   path('ListarCategoria/',ListarCategoria.as_view(), name='ListarCategoria'),     
   path('CrearCategoria/',CrearCategoria.as_view(), name='CrearCategoria'),     
   path('UpdateCategoria/<int:pk>/',UpdateCategoria.as_view(), name='UpdateCategoria'),     
   path('DeleteCategoria/<int:pk>/',DeleteCategoria.as_view(), name='DeleteCategoria'),     


   path('ListarProducto/',ListarProducto.as_view(), name='ListarProducto'),     
   path('CrearProducto/',CrearProducto.as_view(), name='CrearProducto'),     
   path('UpdateProducto/<int:pk>/',UpdateProducto.as_view(), name='UpdateProducto'),     
   path('DeleteProducto/<int:pk>/',DeleteProducto.as_view(), name='DeleteProducto'),     


   path('ListarCliente/',ListarCliente.as_view(), name='ListarCliente'),     
   path('CrearCliente/',CrearCliente.as_view(), name='CrearCliente'),     
   path('UpdateCliente/<int:pk>/',UpdateCliente.as_view(), name='UpdateCliente'),     
   path('DeleteCliente/<int:pk>/',DeleteCliente.as_view(), name='DeleteCliente'),     


   path('ListarVenta/',ListarVenta.as_view(), name='ListarVenta'),     
   path('CrearVenta/',CrearVenta.as_view(), name='CrearVenta'),     
   path('UpdateVenta/<int:pk>/',UpdateVenta.as_view(), name='UpdateVenta'),     
   path('DeleteVenta/<int:pk>/',DeleteVenta.as_view(), name='DeleteVenta'),     


   path('ListarDetVenta/',ListarDetVenta.as_view(), name='ListarDetVenta'),     
   path('CrearDetVenta/',CrearDetVenta.as_view(), name='CrearDetVenta'),     
   path('UpdateDetVenta/<int:pk>/',UpdateDetVenta.as_view(), name='UpdateDetVenta'),     
   path('DeleteDetVenta/<int:pk>/',DeleteDetVenta.as_view(), name='DeleteDetVenta'),     



]