from django.core.mail import send_mail

from users.models import User
from config import settings


def send_user_email(user_item: User):
    send_mail(
        'Подтвердите регистрацию!',
        f'({user_item.email}) Вот сообщение: Ссылка',
        settings.EMAIL_HOST_USER,
        [user_item.email]
    )
