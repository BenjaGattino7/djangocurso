from django.shortcuts import render, redirect
from .forms import formulario
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto=formulario()

    if request.method=="POST":
        formulario_contacto=formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde la app", "el usuario con nombre {} con la direccion {} escribe lo siguiente: {}".format(nombre,email,contenido),"",["benjagattino@outlook.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
                
    return render(request, "contacto/contacto.html",{'miformulario':formulario_contacto})


