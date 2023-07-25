from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido) :

        self.nombre=nombre

        self.apellido=apellido


def saludo(request):

    



    return HttpResponse("Hola")

def fecha(request):

    p1=Persona("Carlos","Ramirez")
    temascurso=["plantillas","modelos","formularios","vistas","deploy"]
    fechaActual =datetime.datetime.now()

    return render(request, "plantilla.html", {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"hora":fechaActual, "temas":temascurso})
    
def calculaEdad(request,edad, age):

    periodo = age-2023    
    edadFutura =edad+periodo
    documento="En el año %s tendras %s años"%(age,edadFutura)

    return HttpResponse(documento)

def cursito(request):
    fechaActual =datetime.datetime.now()

    return render(request, "Cursito.html", {"fechaActual":fechaActual})

def cursitohtml(request):
    fechaActual =datetime.datetime.now()

    return render(request, "Cursohtml.html", {"fechaActual":fechaActual})