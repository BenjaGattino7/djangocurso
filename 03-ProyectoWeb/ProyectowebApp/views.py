from django.shortcuts import render, HttpResponse
from servicios.models import Servicios
# Create your views here.

def home(request):

    return render(request, "ProyectowebApp/home.html")

def servicios(request):
    servicios=Servicios.objects.all()
    return render(request, "ProyectowebApp/servicios.html",{"servicios":servicios})


