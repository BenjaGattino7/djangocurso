
from django.contrib import admin
from django.urls import path
from DjangoCurso.views import saludo, fecha, calculaEdad, cursito, cursitohtml

urlpatterns = [
    
    path('saludo/',saludo),
    path('fecha/',fecha),
    path('edades/<int:edad>/<int:age>', calculaEdad),
    path('cursito/',cursito),
    path('cursohtml/',cursitohtml)
]
