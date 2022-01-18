from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField
from usuarios.models import UserProfile


class Genero(models.TextChoices):
    HOMBRE = "hombre"
    MUJER = "mujer"
    UNISEX = "unisex"


class Categoria(models.TextChoices):
    REMERAS = "Remeras"
    CAMISAS = "Camisas"
    PANTALONES = "Pantalones"
    BERMUDAS = "Bermudas"
    MALLAS = "Mallas"
    CALZADO = "Calzado"
    BUZOS = "Buzos"
    JEANS = "Jeans"
    VARIOS = "Varios"


class Talle(models.TextChoices):
    XXS = "XXS", "Extra extra small"
    XS = "XS", "Extra small"
    S = "S", "Small"
    M = "M", "Medium"
    L = "L", "Large"
    XL = "XL", "Extra large"
    XXL = "XXL", "Extra extra large"


class Producto(models.Model):
    titulo = models.TextField(max_length=30, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    genero = models.CharField(choices=Genero.choices, max_length=6, null=True, blank=True)
    categoria = models.CharField(choices=Categoria.choices, max_length=20, null=True, blank=True, default="varios")
    marca = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    publicado = models.BooleanField(default=False)
    imagen_principal = ImageField(max_length=255, null=True, blank=True, upload_to="media/imagenes/%Y/%m/%d")
    fecha_publicacion = models.DateField(auto_now_add=True)
    hora_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural, verbose_name = u'Producto', u'Productos'

    def __str__(self):
        return str(self.titulo)

    def get_absolute_url(self):
        return reverse('shop_single_product', args=[self.id])


class ProductoTalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    stock = models.IntegerField(default=0)
    talle = models.CharField(max_length=3, choices=Talle.choices)
    fecha_ingreso = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = "producto", "talle"

    def __str__(self):
        return "{} ({})".format(self.producto.titulo, self.talle)


class Comentario(models.Model):
    producto = models.ForeignKey(Producto, related_name="comentarios", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255)
    texto = models.TextField()
    fechora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.producto.titulo, self.nombre)


class Carrito(models.Model):
    usuario = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def total(self):
        lineas_pedidos = LineaPedido.objects.all().filter(carrito=self.id)
        total = 0.0
        for lp in lineas_pedidos:
            total += int(lp.cantidad * lp.producto_talle.producto.precio)
        return total


class LineaPedido(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto_talle = models.ForeignKey(ProductoTalle, models.CASCADE)
    cantidad = models.IntegerField()
    #subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)




