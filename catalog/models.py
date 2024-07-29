from django.db import models

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

    def __str__(self):
        return (f'Название: {self.name} / '
                f'Описание: {self.description} / '
                f'Превью: {self.preview} / '
                f'Категория: {self.category} / '
                f'Цена: {self.price} / '
                f'Создан: {self.created_at} / '
                f'Изменён: {self.updated_at}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    def __str__(self):
        return (f'Наименование: {self.name} / '
                f'Описание: {self.description}')

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


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='Контент')
    preview = models.ImageField(upload_to='blog/%Y/%m/%d/', default='blog/none.jpg',
                                verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотров')

    def __str__(self):
        return (f'Название: {self.name} / '
                f'Slug: {self.slug} / '
                f'Содержимое: {self.content} / '
                f'Изображение: {self.preview} / '
                f'Создан: {self.created_at} / '
                f'Статус: {self.is_published} / '
                f'Количество просмотров: {self.views_count}')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('created_at',)
