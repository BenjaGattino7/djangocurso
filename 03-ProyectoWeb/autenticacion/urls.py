from django.urls import include, path
from . import views
from .views import VRegistro, cerrar_sesion, inicio_sesion , autenticar


urlpatterns = [

   path('',VRegistro.as_view(), name="Autenticacion"),
   
   path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),

   path('inicio_sesion',inicio_sesion, name="inicio_sesion"),

   path('autenticar', autenticar, name="autenticar")

]
