from django.test import TestCase
from .models import Producto,Marca,Contacto

# Create your tests here.
class TestViews(TestCase):
  
#Preparar las los objetos para realizar las pruebas
    def setUp(self):
        self.m1 = Marca.objects.create(
            nombre = 'marca test',

        )
        self.p1 = Producto.objects.create(
            nombre = 'nombre test',
            Precio = 1000,
            descripcion = 'descripcion test',
            marca = self.m1,
            imagen = None
        )

        self.f1 = Contacto.objects.create(
          nombre = 'Test contacto',
          correo = 'Test@gmail.com',
          telefono = '12341234',
          tipo_consulta = 2,
          comentario = 'test nuevo'
        )
#Veificar que se a creado un objeto de tipo Contacto
    def test_contacto(self): 
      resul = Contacto.objects.filter(nombre='Test contacto')
      self.assertNotEqual(resul,self.f1)

#Verifica que la funcion de descuento se aplique a los productos
    def test_calcular_descuento(self):
        descuento = self.p1.descuento()
        self.assertEquals(800,descuento)
    
    