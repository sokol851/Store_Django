from django import template

register = template.Library()


# Создание тега
@register.simple_tag
def refactor(preview):
    if preview:
        return f'/media/{preview}'
    return '#'


@register.simple_tag
def get_value(dict, key):
    return dict.get(key)
