from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Producto, ProductoTalle, Comentario, Carrito, LineaPedido


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

    def test_create_productotalle(self):
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

    def test_create_productotalle_without_producto(self):
        """ Test creacion ProductoTalle con valor Producto relacionado inválido """

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
        """ Test creacion Comentario con valor Producto relacionado inválido """

        email = "test@test.com"
        texto = "Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum"

        with self.assertRaises(ValueError):
            Comentario.objects.create(
                producto=1,
                email=email,
                texto=texto
            )

    def test_create_carrito(self):
        """ Test creacion Carrito """

        email = 'test@prueba.com'
        password = 'Testpass123'
        nombre = 'nombreprueba'
        apellido = 'apellidoprueba'
        usuario = get_user_model().objects.create_user(
            email=email,
            password=password,
            nombre=nombre,
            apellido=apellido
        )

        activo = False

        carrito = Carrito.objects.create(
            usuario=usuario,
            activo=activo
        )

        self.assertEqual(carrito.usuario, usuario)
        self.assertEqual(carrito.activo, activo)

    def test_create_carrito_without_user(self):
        """ Test crear Carrito con valor Usuario relacionado inválido """

        with self.assertRaises(ValueError):
            Carrito.objects.create(usuario=1)

    def test_create_linea_pedido(self):
        """ Test crear LineaPedido """

        email = 'test@prueba.com'
        password = 'Testpass123'
        nombre = 'nombreprueba'
        apellido = 'apellidoprueba'
        usuario = get_user_model().objects.create_user(
            email=email,
            password=password,
            nombre=nombre,
            apellido=apellido
        )
        carrito = Carrito.objects.create(
            usuario=usuario
        )

        titulo = "camisaprueba"
        producto = Producto.objects.create(
            titulo=titulo
        )

        talle = "Small"
        producto_talle = ProductoTalle.objects.create(
            producto=producto,
            talle=talle)

        cantidad = 20
        linea_pedido = LineaPedido.objects.create(
            carrito=carrito,
            producto_talle=producto_talle,
            cantidad=cantidad
        )

        self.assertEqual(linea_pedido.carrito, carrito)
        self.assertEqual(linea_pedido.producto_talle, producto_talle)
        self.assertEqual(linea_pedido.cantidad, cantidad)