# Generated by Django 4.0.5 on 2022-07-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HildaApp', '0014_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]
