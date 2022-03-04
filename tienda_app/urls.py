from django.urls import path
from tienda_app.views.inicio import *
from tienda_app.views.producto import *
from tienda_app.views.informacion import *
from tienda_app.views.contacto import *
from tienda_app.views.registro import *

urlpatterns = [
    path('', tienda_inicio, name="tienda_inicio"),
    path('productos/', tienda_producto, name="tienda_producto"),
    path('informacion/', tienda_informacion, name="tienda_informacion"),
    path('contactanos/', tienda_contacto, name="tienda_contacto"),
    path('registro/', registro, name="registro"),
]
