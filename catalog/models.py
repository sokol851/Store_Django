from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    date_edited = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return (f'Наименование: {self.name}\n'
                f'Описание: {self.description}\n'
                f'Изображение: {self.description}\n'
                f'Категория: {self.category}\n'
                f'Цена: {self.price}\n'
                f'Дата создания: {self.date_create}\n'
                f'Дата изменения: {self.date_edited}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return (f'Наименование: {self.name}\n'
                f'Описание: {self.description}')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)
