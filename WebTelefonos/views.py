
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactoForms
from .models import Contacto


def base(request):  
    return render(request,'web/base.html') 

def inicio(request):
    return render(request,'web/inicio.html')

def celulares(request):
    return render(request,'web/celulares.html')


def sobrenos(request):
    return render(request,'web/sobre_nos.html')

def accesorios(request):
    return render(request,'web/accesorios.html')

def samsung(request):
    return render(request,'web/samsung.html')

def huawei(request):
    return render(request,'web/huawei.html')

def apple(request):
    return render(request,'web/apple.html')

def oferta(request):
    return render(request,'web/ofertas.html')



def contacto(request):
    data = {
        'form': ContactoForms()
    } 

    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado" 
        else: 
            data["form"] = formulario    
    return render(request, 'web/contacto.html', data)    