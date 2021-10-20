from django import forms
from .models import Comentario, Producto, Talle, LineaProducto
from django.forms import TextInput, Textarea


class ProductoCarritoForm(forms.ModelForm):
    cantidad = forms.IntegerField()

    class Meta:
        model = LineaProducto
        fields = ['carrito', 'producto_talle', 'cantidad']

        widgets = {
            'carrito': forms.HiddenInput(),
            'producto': forms.HiddenInput(),
            'cantidad': forms.IntegerField(min_value=1),
        }


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nombre', 'apellido', 'email', 'texto', 'producto']

        widgets = {
            'producto': forms.HiddenInput(),
            'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre"}),
            'apellido': TextInput(attrs={'class': 'form-control', 'placeholder': "Apellido"}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            'texto': Textarea(attrs={'class': 'form-control', 'placeholder': "Comentario..."}),
        }


ORDEN_CHOICES = [
    ('MR', 'Más recientes'),
    ('MA', 'Más antiguos'),
    ('MaP', 'Mayor precio'),
    ('MeP', 'Menor precio'),
]


class FiltroForm(forms.ModelForm):
    orden = forms.ChoiceField(choices=ORDEN_CHOICES)

    class Meta:
        model = Producto
        fields = ['orden', 'genero', 'categoria']

        widgets = {
            'orden': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nombre', 'email', 'texto']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Tu Nombre"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Tu Email"}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Tu Mensaje"}),
        }
