# Generated by Django 3.2.7 on 2022-01-03 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Echango', '0003_alter_lineapedido_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineapedido',
            name='total',
        ),
    ]
