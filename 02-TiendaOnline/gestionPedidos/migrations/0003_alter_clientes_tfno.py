# Generated by Django 4.0.4 on 2023-06-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='tfno',
            field=models.CharField(max_length=20, verbose_name='Telefono'),
        ),
    ]