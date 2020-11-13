from django import forms
from .models import Contacto, Producto
from django.forms import ValidationError

class ContactoForms(forms.ModelForm):

    #creacion de formulario contacto

    nombre = forms.CharField(min_length=5 ,max_length=20)
    
    class Meta:
        model = Contacto
        fields = ["nombre","correo","telefono","tipo_consulta","comentario"] 