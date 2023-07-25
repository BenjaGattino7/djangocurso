from django import forms

class formulario(forms.Form):

    nombre=forms.CharField(label="Tu nombre",required=True)
    email=forms.CharField(label="Email",required=True)
    contenido= forms.CharField(label="contenido",widget=forms.Textarea)