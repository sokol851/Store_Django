from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='catalog/%Y/%m/%d/', default='catalog/none.jpg',
                                verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="владелец", **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Contacts(models.Model):
    warehouse_address = models.CharField(max_length=100, verbose_name='Адрес склада')
    legal_address = models.CharField(max_length=100, verbose_name='Юридический адрес')
    working_hours = models.CharField(max_length=100, verbose_name='Время работы')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Электронная почта')

    def __str__(self):
        return (f'Адрес склада: {self.warehouse_address} / '
                f'Юридический адрес: {self.legal_address} / '
                f'Время работы: {self.working_hours} / '
                f'Телефон: {self.phone} / '
                f'Электронная почта: {self.email}')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(max_length=150, verbose_name='Электронный адрес (email)')
    content = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Вам письмо от {self.email}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name='Продукт',
                                **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='Название версии')
    number_version = models.IntegerField(verbose_name='Номер версии', **NULLABLE)
    is_current = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.title} ({self.number_version})'

    class Meta:
        ordering = ['-is_current', 'number_version']
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
