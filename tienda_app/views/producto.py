from django.db.models.expressions import F
from imagen_producto_marca_app.models import ImagenProductoMarca
from producto_marca_app.models import ProductoMarca, producto_marca
from django.shortcuts import render

# Create your views here.


def tienda_producto(request):
    productos = ProductoMarca.objects.all().order_by('nombre')
    data = {'productos': preparar_lista(productos)}
    return render(request, 'tienda_app/producto/base.html', data)


def preparar_lista(self):
    for p in self:
        setattr(p, 'imagen', ImagenProductoMarca.objects.filter(
            producto_marca=p.uuid).first())
    return self
