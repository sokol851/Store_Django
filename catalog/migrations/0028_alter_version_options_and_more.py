# Generated by Django 5.0.7 on 2024-08-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_alter_version_options_alter_version_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ['-is_current', 'number_version'], 'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.RemoveConstraint(
            model_name='version',
            name='unique_active_version',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='is_active',
            new_name='is_current',
        ),
        migrations.AddConstraint(
            model_name='version',
            constraint=models.UniqueConstraint(condition=models.Q(('is_current', True)), fields=('product', 'is_current'), name='unique_current_version'),
        ),
    ]