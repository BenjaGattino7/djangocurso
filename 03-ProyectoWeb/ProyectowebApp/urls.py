from django.urls import include, path

from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
   path('',views.home, name="Inicio"),
   path('servicios/',views.servicios, name="Servicios"), 


]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)