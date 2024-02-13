from django import forms

# Create your models here.

class Form_test1(forms.Form):
    nombre1 = forms.CharField(max_length=40)
    cantidad1 = forms.IntegerField()
    
class Form_test2(forms.Form):
    nombre2 = forms.CharField(max_length=30)
    cantidad2 = forms.IntegerField()

class Form_test3(forms.Form):
    nombre3 = forms.CharField(max_length=20)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()