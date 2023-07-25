from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def busquedaProductos (request):

    return render(request, "busqueda.html")


def buscar(request):
    if request.GET["prd"]:

        mensaje="Articulo buscado: %r " %request.GET["prd"]
        producto=request.GET["prd"]

        articulos=Articulos.objects.filter(nombre__icontains=producto)

        return render(request, "resultados.html", {"articulos":articulos,"query":producto})
    
    else:
        mensaje="No se han realizado busquedas"
        return HttpResponse(mensaje)

@csrf_exempt
def contacto(request):

        if request.method=="POST":
             
            subject=request.POST["asunto"]

            message=request.POST ["mensaje"] + " " + request.POST["email"]

            email_from= settings.EMAIL_HOST_USER

            box_list=["bgattino7@gmail.com"]

            send_mail(subject,message,email_from,box_list,fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)      

            return render(request, "contacto-enviado.html")

        return render(request, "contacto.html")
    