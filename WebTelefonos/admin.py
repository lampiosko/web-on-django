from django.contrib import admin
from .models import Marca, Producto,Contacto

admin.site.register(Contacto)
admin.site.register(Marca)
admin.site.register(Producto)