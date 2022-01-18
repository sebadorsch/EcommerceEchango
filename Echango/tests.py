from django.test import TestCase
from .models import Producto, ProductoTalle, Comentario


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

    def test_create_new_productotalle(self):
        """ Test creacion nuevo ProductoTalle """

        titulo = "camisaprueba"
        talle = "Small"
        producto = Producto.objects.create(titulo=titulo)

        producto_talle = ProductoTalle.objects.create(
            producto=producto,
            talle=talle
        )

        self.assertEqual(producto_talle.producto, producto)
        self.assertEqual(producto_talle.talle, talle)

    def test_create_new_productotalle_without_producto(self):
        """ Test creacion ProductoTalle con Producto relacionado inválido """

        producto = 1
        talle = "Small"

        with self.assertRaises(ValueError):
            ProductoTalle.objects.create(
                producto=producto,
                talle=talle
            )

    def test_create_comentario(self):
        """ Test creacion Comentario """

        titulo = "camisaprueba"
        producto = Producto.objects.create(titulo=titulo)
        email = "test@test.com"
        texto = "Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum"

        comentario = Comentario.objects.create(
            producto=producto,
            email=email,
            texto=texto
        )
        self.assertEqual(comentario.producto, producto)
        self.assertEqual(comentario.email, email)
        self.assertEqual(comentario.texto, texto)

    def test_create_comentario_without_producto(self):
        """ Test creacion Comentario sin producto relacionado """

        email = "test@test.com"
        texto = "Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum"

        with self.assertRaises(ValueError):
            Comentario.objects.create(
                producto=1,
                email=email,
                texto=texto
            )
