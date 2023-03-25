from django.db import models

from django.contrib.auth.models import User

class Empresa(models.Model):
    idEMPRESA = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fk_gerente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Bus(models.Model):
    idBUS = models.AutoField(primary_key=True)
    capacidad = models.IntegerField()
    num_bus = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)
    climatizado = models.BooleanField(default=False)
    fk_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.num_bus}"

    
class Ruta(models.Model):
    idRUTA = models.AutoField(primary_key=True)
    region = models.CharField(max_length=45)
    descripcion = models.TextField()

    def __str__(self):
        return self.region
    
class Viaje(models.Model):
    idVIAJE = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=45)
    destino = models.CharField(max_length=45)
    fecha_hora = models.DateTimeField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    clase = models.CharField(max_length=45)
    cupo = models.IntegerField()
    fk_bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    fk_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)

    def __str__(self):
        return self.destino
    
class Usuarios(models.Model):
    idUSUARIOS = models.AutoField(primary_key=True)
    user = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField()

    def __str__(self):
        return self.name

