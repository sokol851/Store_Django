import json
from django.core.management import BaseCommand
from catalog.models import Category, Product, Contacts, Version
from companies.models import Companies
from blog.models import Blog

from config.settings import BASE_DIR


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open(BASE_DIR / 'fixtures' / 'category_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_read_products():
        with open(BASE_DIR / 'fixtures' / 'product_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_read_contacts():
        with open(BASE_DIR / 'fixtures' / 'contacts_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_read_blog():
        with open(BASE_DIR / 'fixtures' / 'blog_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_read_companies():
        with open(BASE_DIR / 'fixtures' / 'companies_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def json_read_versions():
        with open(BASE_DIR / 'fixtures' / 'versions_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    def handle(self, *args, **options):
        # Удаляем продукты, потом категории
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contacts.objects.all().delete()
        Blog.objects.all().delete()
        Companies.objects.all().delete()
        Version.objects.all().delete()

        # Создаём списки для объектов.
        category_for_create = []
        product_for_create = []
        contacts_for_create = []
        blog_for_create = []
        companies_for_create = []
        versions_for_create = []

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
                                              updated_at=product['fields']['updated_at'],
                                              slug=product['fields']['slug']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        # Обход фикстуры контактов
        for contact in Command.json_read_contacts():
            contacts_for_create.append(Contacts(pk=contact['pk'],
                                                warehouse_address=contact['fields']['warehouse_address'],
                                                legal_address=contact['fields']['legal_address'],
                                                working_hours=contact['fields']['working_hours'],
                                                phone=contact['fields']['phone'],
                                                email=contact['fields']['email']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Contacts.objects.bulk_create(contacts_for_create)

        # Обход фикстуры блогов
        for blog in Command.json_read_blog():
            blog_for_create.append(Blog(pk=blog['pk'],
                                        name=blog['fields']['name'],
                                        slug=blog['fields']['slug'],
                                        content=blog['fields']['content'],
                                        preview=blog['fields']['preview'],
                                        created_at=blog['fields']['created_at'],
                                        is_published=blog['fields']['is_published'],
                                        views_count=blog['fields']['views_count']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Blog.objects.bulk_create(blog_for_create)

        # Обход фикстуры компаний
        for company in Command.json_read_companies():
            companies_for_create.append(Companies(pk=company['pk'],
                                                  title=company['fields']['title'],
                                                  description=company['fields']['description'],
                                                  views_count=company['fields']['views_count'],
                                                  is_published=company['fields']['is_published'],
                                                  slug=company['fields']['slug']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Companies.objects.bulk_create(companies_for_create)

        # Обход фикстуры версий
        for version in Command.json_read_versions():
            versions_for_create.append(Version(pk=version['pk'],
                                               product=Product.objects.get(pk=version['fields']['product']),
                                               title=version['fields']['title'],
                                               number_version=version['fields']['number_version'],
                                               is_current=version['fields']['is_current']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Version.objects.bulk_create(versions_for_create)
