# Generated by Django 4.0.5 on 2022-06-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HildaApp', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.CharField(default=10, max_length=20, verbose_name='Stock'),
            preserve_default=False,
        ),
    ]