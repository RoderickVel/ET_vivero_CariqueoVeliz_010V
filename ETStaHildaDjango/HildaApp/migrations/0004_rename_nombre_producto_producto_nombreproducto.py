# Generated by Django 4.0.5 on 2022-06-12 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HildaApp', '0003_producto_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_producto',
            new_name='nombreproducto',
        ),
    ]
