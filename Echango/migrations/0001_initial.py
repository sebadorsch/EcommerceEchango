# Generated by Django 3.2.7 on 2022-01-24 22:05

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, max_length=30, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('unisex', 'Unisex')], max_length=6, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Remeras', 'Remeras'), ('Camisas', 'Camisas'), ('Pantalones', 'Pantalones'), ('Bermudas', 'Bermudas'), ('Mallas', 'Mallas'), ('Calzado', 'Calzado'), ('Buzos', 'Buzos'), ('Jeans', 'Jeans'), ('Varios', 'Varios')], default='varios', max_length=20, null=True)),
                ('marca', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('publicado', models.BooleanField(default=False)),
                ('imagen_principal', sorl.thumbnail.fields.ImageField(blank=True, max_length=255, null=True, upload_to='media/imagenes/%Y/%m/%d')),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('hora_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='ProductoTalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0)),
                ('talle', models.CharField(choices=[('XXS', 'Extra extra small'), ('XS', 'Extra small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large'), ('XXL', 'Extra extra large')], max_length=3)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Echango.producto')),
            ],
        ),
        migrations.CreateModel(
            name='LineaPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Echango.carrito')),
                ('producto_talle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Echango.productotalle')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('texto', models.TextField()),
                ('fechora', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Echango.producto')),
            ],
        ),
    ]
