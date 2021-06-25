from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.correo)

    def obtener_costo_telefonos(self):
        valor = [t.costo_plan for t in self.numeros_telefonicos.all()]
        valor = sum(valor)
        return valor

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    costo_plan = models.DecimalField(max_digits=100, decimal_places=2)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
