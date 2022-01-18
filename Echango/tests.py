from django.test import TestCase
from .models import Producto


class ModelTest(TestCase):

    def test_create_producto(self):
        """ Test para creacion de nuevo producto solo con el titulo """
        titulo = "camisaprueba"

        producto = Producto.objects.create(
            titulo=titulo
        )

        self.assertEqual(producto.titulo, titulo)

    def test_create_producto_completo(self):
        """ Test para creacion de nuevo producto con todos los campos """
        titulo = "camisaprueba"
        descripcion = "camisapruebacamisapruebacamisapruebacamisapruebacamisapruebacamisapruebacamisapruebacamisaprueba"
        genero = "unisex"
        categoria = "Camisas"
        marca = "marcaprueba"
        color = "colorprueba"
        precio = 1500
        publicado = True

        producto = Producto.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            genero=genero,
            categoria=categoria,
            marca=marca,
            color=color,
            precio=precio,
            publicado=publicado
        )

        self.assertEqual(producto.titulo, titulo)
        self.assertEqual(producto.descripcion, descripcion)
        self.assertEqual(producto.genero, genero)
        self.assertEqual(producto.categoria, categoria)
        self.assertEqual(producto.marca, marca)
        self.assertEqual(producto.color, color)
        self.assertEqual(producto.precio, precio)
        self.assertEqual(producto.publicado, publicado)