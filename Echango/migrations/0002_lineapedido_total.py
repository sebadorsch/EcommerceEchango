# Generated by Django 3.2.7 on 2022-01-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Echango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineapedido',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
