# Generated by Django 5.1 on 2024-11-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_caracteristica_categoria_marca_producto_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]