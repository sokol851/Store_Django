# Generated by Django 5.0.7 on 2024-07-21 12:56

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=(pathlib.PureWindowsPath('D:/win/Store_Django/media'), pathlib.PureWindowsPath('D:/win/Store_Django/catalog/media')), verbose_name='Изображение'),
        ),
    ]