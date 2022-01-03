from django.contrib import admin
from .models import Producto, ProductoTalle, Comentario, Carrito, LineaPedido

admin.site.register(Producto)
admin.site.register(ProductoTalle)
admin.site.register(Comentario)
admin.site.register(Carrito)
admin.site.register(LineaPedido)
