from django.urls import include, path

from .import views

urlpatterns = [

   path('',views.tienda, name="Tienda"),

]


