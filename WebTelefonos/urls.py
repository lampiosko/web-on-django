from django.urls import path
from . import views

#Mapeo de las rutas URL segun las paginas(templates)
urlpatterns = [
    path('', views.inicio, name="inicio" ),
    path('celulares/', views.celulares,name="celulares"),
    path('contacto/', views.contacto,name="contacto"),
    path('nosotros/', views.sobrenos,name="nosotros"),
    path('accesorios/', views.accesorios,name="accesorios"),
    path('samsung/', views.samsung,name="samsung"),
    path('apple/', views.apple,name="apple"),
    path('huawei/', views.huawei,name="huawei"),
    path('ofertas/', views.oferta,name="oferta"),
    
]