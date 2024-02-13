from django.shortcuts import render
from APP1.models import test1,test2,test3
from APP1.forms import Form_test1, Form_test2, Form_test3
from django.http import HttpResponse
from django.template import loader

def Mod1(request):
    if request.method == "POST":
            miFormulario = Form_test1(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = test1(nombre=informacion["nombre1"], camada=informacion["cantidad1"])
                  curso.save()
                  return render(request, "APP1/mod1.html")
    else:
            miFormulario = Form_test1()
    return render(request, "APP1/mod1.html", {"miFormulario": miFormulario})


def Mod2(request):
    if request.method == "POST":
            miFormulario = Form_test2(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = test2(nombre=informacion["nombre2"], camada=informacion["cantidad2"])
                  curso.save()
                  return render(request, "APP1/mod2.html")
    else:
            miFormulario = Form_test2()
    return render(request, "APP1/mod2.html", {"miFormulario": miFormulario})

def Mod3(request):
    ##plantilla = loader.get_template('mod3.html')
    ##documento = plantilla.render()
	##return render(request, "APP1/mod3.html")
    
    ##if request.GET['nombre1']:
    ##    nombre1 = request.GET['nombre1']
    ##    cantidadt = models.test1.objects.filter(cantidad1__icontains=cantidadt)
    ##    return render(request, 'APP1/mod3.html', {'nombre1': nombre1, 'cantidad1': cantidadt})
    ##else:
    ##    respuesta = 'No enviaste datos'

    ##return render(request, 'APP1/mod3.html', {'respuesta': respuesta})
    if request.method == "POST":
        update = test1(request.post["nombre1"], request.post["cantidad1"])
        update.save()
    return render(request, 'APP1/mod3.html')

# Create your views here.
