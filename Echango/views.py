from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Producto, Categoria, ProductoTalle, Comentario, LineaPedido, Carrito
from .forms import ComentarioForm, FiltroForm, ContactoForm, LineaPedidoForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse


def home(request, template_name="index_shop.html"):
    args = {}
    productos = Producto.objects.all().filter(publicado=True)
    args.update({'productos': productos})

    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        if contacto_form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            texto = request.POST.get('texto')
            try:
                send_mail(
                    'Mensaje de ' + nombre,             #subject
                    texto,                              #messaje
                    email,                              #from
                    ['sebastian.adorsch@gmail.com'],    #to
                )
            except BadHeaderError:
                return HttpResponse('Invalid email error')

            args.update({'nombre': nombre})
            return render(request, template_name, args)
    else:
        contacto_form = ContactoForm()
    args.update({'contacto_form': contacto_form})

    return render(request, template_name, args)


def about_us(request, template_name="about_us.html"):

    return render(request, template_name)


def shop_product_col_3(request, template_name="shop_product_col_3.html"):
    args = {}
    producto = Producto.objects.all()
    productos = Producto.objects.all()

    if request.method == 'GET':
        form = FiltroForm(request.GET)
        orden = request.GET.get('orden')
        genero = request.GET.get('genero')
        categoria = request.GET.get('categoria')
        if orden:
            if orden == 'MR':
                producto = producto.filter().order_by('fecha_publicacion')
            if orden == 'MA':
                producto = producto.filter().order_by('-fecha_publicacion')
            if orden == 'MaP':
                producto = producto.filter().order_by('-precio')
            if orden == 'MeP':
                producto = producto.filter().order_by('precio')
        if genero:
            producto = producto.filter(genero=genero)
        if categoria:
            producto = producto.filter(categoria=categoria)

    args.update({'producto': producto,
                 'productos': productos,
                 'form': form})

    return render(request, template_name, args)


def shop_product_col_3_categoria(request, categoria, template_name="shop_product_col_3.html"):
    args = {}
    categoria = categoria.capitalize()
    producto = Producto.objects.all().filter(categoria=categoria, publicado=True)
    productos = Producto.objects.all()

    args.update({'producto': producto, 'productos': productos})

    return render(request, template_name, args)


def shop_single_product(request, producto_id, template_name="shop_single_product.html", ):
    args = {}

    carrito, creado = Carrito.objects.get_or_create(usuario=request.user, activo=True)
    producto = get_object_or_404(Producto, pk=producto_id, publicado=True)
    productos_talle = ProductoTalle.objects.all().filter(producto_id=producto_id)
    productos = (Producto.objects.all().filter(publicado=True)).exclude(id=producto_id)
    comentarios = Comentario.objects.all().filter(producto_id=producto_id)
    total_comentarios = comentarios.count()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        linea_pedido_form = LineaPedidoForm(request.POST, producto=producto)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect(reverse('shop_single_product', kwargs={'producto_id': producto.id}))
        elif linea_pedido_form.is_valid():
            new_linea_pedido = linea_pedido_form.save(commit=False)
            return redirect(reverse('shop_checkout'))
    else:
        comentario_form = ComentarioForm(initial={'producto': producto})
        linea_pedido_form = LineaPedidoForm(initial={'carrito': carrito}, producto=producto)

    args.update({'producto': producto,
                 'productos': productos,
                 'comentarios': comentarios,
                 'total_comentarios': total_comentarios,
                 'productos_talle': productos_talle,
                 'comentario_form': comentario_form,
                 'linea_pedido_form': linea_pedido_form,
                 })
    return render(request, template_name, args)


def login_register(request, template_name):
    return render(request, template_name)


def shop_checkout(request, template_name='shop_checkout.html'):
    args = {}
    productos = Producto.objects.all().filter(publicado=True)
    args.update({'productos': productos})
    return render(request, template_name, args)

#
# def carrito(request, carrito_id, template_name='shop_checkout.html'):
#     args = {}
#     productos = Producto.objects.all().filter(publicado=True)
#     args.update({'productos': productos})
#     return render(request, template_name, args)
#
