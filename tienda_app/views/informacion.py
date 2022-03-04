from django.shortcuts import render

# Create your views here.

def tienda_informacion(request):
    return render(request,'tienda_app/informacion/base.html')
