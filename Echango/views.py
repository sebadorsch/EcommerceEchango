from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, ProductoTalle, Comentario, Carrito
from .forms import ComentarioForm, FiltroForm, ContactoForm, ProductoCarritoForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.mail import send_mail


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

            send_mail(
                'Mensaje de ' + nombre,
                texto,
                email,
                ['sebastian_dorsch@hotmail.com'],
            )
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
            pass
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

    producto = get_object_or_404(Producto, pk=producto_id, publicado=True)
    productos_talle = ProductoTalle.objects.all().filter(producto_id=producto_id)
    productos = (Producto.objects.all().filter(publicado=True)).exclude(id=producto_id)
    comentarios = Comentario.objects.all().filter(producto_id=producto_id)
    total_comentarios = comentarios.count()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        carrito_form = ProductoCarritoForm(request.POST)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect(home)
        elif carrito_form.is_valid():
            carrito_form.save()
            return redirect(home)
    else:
        comentario_form = ComentarioForm(initial={'producto': producto})
        carrito_form = ProductoCarritoForm(initial={'usuario': request.user, 'producto': producto})

    args.update({'producto': producto,
                 'productos': productos,
                 'comentarios': comentarios,
                 'total_comentarios': total_comentarios,
                 'productos_talle': productos_talle,
                 'comentario_form': comentario_form,
                 'carrito_form': carrito_form,
                 })
    return render(request, template_name, args)


def shop_checkout(request, template_name='shop_checkout.html'):
    args = {}
    productos = (Producto.objects.all().filter(publicado=True))
    args.update({'productos': productos})
    return render(request, template_name, args)


def login_register(request, template_name):
    return render(request, template_name)


def carrito(request, template_name='shop_checkout.html'):
    return render(request, template_name)


