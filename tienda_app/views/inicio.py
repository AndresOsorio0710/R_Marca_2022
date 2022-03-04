from django.shortcuts import render

# Create your views here.

def tienda_inicio(request):
    return render(request,'tienda_app/inicio/base.html')
