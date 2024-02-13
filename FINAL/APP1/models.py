from django.db import models

# Create your models here.

class test1(models.Model):
    nombre1 = models.CharField(max_length=40)
    cantidad1 = models.IntegerField()
    
class test2(models.Model):
    nombre2 = models.CharField(max_length=30)
    cantidad2 = models.IntegerField()

class test3(models.Model):
    nombre3 = models.CharField(max_length=20)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()