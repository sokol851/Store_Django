from django.core.cache import cache
from django.conf import settings


def get_data_from_cache(model, name_list: str):
    if settings.CACHE_ENABLED:
        if cache.get(name_list):
            subject_list = cache.get(name_list)
            print(f'Получено значение из кеша:{subject_list}')
        else:
            subject_list = model.objects.all()
            cache.set(name_list, subject_list)
            print(f'Присвоено новое значение в кеш:{subject_list}')
    else:
        subject_list = model.objects.all()
        print('Кеширование отключено!')
    return subject_list
