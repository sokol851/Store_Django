# Generated by Django 5.0.7 on 2024-07-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_edited',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
    ]