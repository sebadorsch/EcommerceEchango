from django.contrib import admin
from .models import Producto, ProductoTalle, Comentario, Carrito

admin.site.register(Producto)
admin.site.register(ProductoTalle)
admin.site.register(Comentario)
admin.site.register(Carrito)
