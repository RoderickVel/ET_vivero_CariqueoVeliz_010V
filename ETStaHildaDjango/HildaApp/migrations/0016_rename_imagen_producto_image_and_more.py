# Generated by Django 4.0.5 on 2022-07-15 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HildaApp', '0015_alter_producto_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombreproducto',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='price',
        ),
    ]
