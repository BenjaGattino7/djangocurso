# Generated by Django 4.0.4 on 2023-07-12 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_categoriaprod_updated_producto_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriaprod',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Precio',
            new_name='precio',
        ),
    ]
