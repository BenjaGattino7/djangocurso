from django.urls import include, path

from .import views

urlpatterns = [

   path('',views.procesar_pedido, name="procesar-pedido"),

]


