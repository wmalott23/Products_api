# Generated by Django 4.0.3 on 2022-03-31 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='inventory_quanitity',
            new_name='inventory_quantity',
        ),
    ]
