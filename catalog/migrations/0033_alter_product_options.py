# Generated by Django 4.2.15 on 2024-08-17 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('set_published', 'Can publish Продукт')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
