# Generated by Django 5.0.7 on 2024-08-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_version_delete_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='description',
        ),
        migrations.AddField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='version',
            name='number_version',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название версии'),
        ),
    ]
