from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE, help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/%Y', default='users/non_avatar.png', verbose_name='аватар', **NULLABLE,
                               help_text='Загрузите свой аватар')
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE, help_text='Укажите вашу страну')
    is_active = models.BooleanField(default=False)

    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
