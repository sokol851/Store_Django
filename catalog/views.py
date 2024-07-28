from django.shortcuts import render
from .models import Contacts, Product, Category


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/index.html', context)


def contacts(request):
    about = Contacts.objects.all()
    context = {'about': about}
    return render(request, 'main/contacts.html', context)


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'main/feedback.html')


def product_page(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'main/product_page.html', context)


def create_product(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_pk = int(request.POST.get('category'))
        category = Category.objects.get(pk=category_pk)
        # preview = request.POST.get('preview')
        price = request.POST.get('price')
        product_dict = {'name': name, 'description': description,
                        'category': category,
                        'price': price}
        Product.objects.create(**product_dict)
    return render(request, 'main/create_product.html', context)
