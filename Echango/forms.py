from django import forms
from .models import Comentario, Producto, Talle, LineaPedido, ProductoTalle
from django.forms import TextInput, Textarea


class LineaPedidoForm(forms.ModelForm):

    class Meta:
        model = LineaPedido
        fields = ['carrito', 'producto_talle', 'cantidad']

        widgets = {
            "carrito": forms.HiddenInput,
            "producto_talle": forms.Select(attrs={"class": 'form-control'}),
            "cantidad": forms.TextInput(attrs={"class": 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        producto = kwargs.pop('producto')
        super(LineaPedidoForm, self).__init__(*args, **kwargs)
        self.fields['producto_talle'].queryset = ProductoTalle.objects.filter(producto=producto)


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
    orden = forms.ChoiceField(choices=ORDEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Producto
        fields = ['orden', 'genero', 'categoria']

        widgets = {
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
