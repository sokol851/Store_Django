import json
from django.core.management import BaseCommand
from catalog.models import Category, Product

from config.settings import BASE_DIR


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open(BASE_DIR / 'fixtures' / 'category_data.json') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_read_products():
        with open(BASE_DIR / 'fixtures' / 'product_data.json') as json_file:
            data = json.load(json_file)
            return data

    def handle(self, *args, **options):
        # Удаляем продукты, потом категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаём списки для объектов.
        category_for_create = []
        product_for_create = []

        # Обход фикстуры категорий
        for category in Command.json_read_categories():
            category_for_create.append(Category(pk=category['pk'], name=category['fields']['name'],
                                                description=category['fields']['description']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обход фикcтуры продуктов
        for product in Command.json_read_products():
            product_for_create.append(Product(pk=product['pk'], name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              preview=product['fields']['preview'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at'], ))
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
