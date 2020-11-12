from django.db import models

#inicio tabla contacto
opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=9)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    comentario = models.TextField()

    def __str__(self):
        return self.nombre


# inicio tabla marca

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
#termino tabla marca

#inicio tabla Producto

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre

#termino tabla producto