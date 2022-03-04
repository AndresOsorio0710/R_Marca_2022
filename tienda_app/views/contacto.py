from django.shortcuts import render

# Create your views here.

def tienda_contacto(request):
    return render(request,'tienda_app/contacto/base.html')
