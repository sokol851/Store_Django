# Generated by Django 5.0.7 on 2024-07-20 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_manufactured_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='manufactured_at',
        ),
    ]
