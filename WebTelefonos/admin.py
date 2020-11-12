from django.contrib import admin
from .models import Marca,Producto,Contacto

class ProductoAdmin(admin.ModelAdmin):
  list_display = ["nombre","Precio","marca"]
  list_editable = ["Precio"]
  search_fields = ["nombre"]
  list_filter = ["marca"]

admin.site.register(Contacto)
admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)