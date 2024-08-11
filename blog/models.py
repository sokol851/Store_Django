from django.db import models

from catalog.models import NULLABLE


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
