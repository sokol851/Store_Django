from django.shortcuts import render
from .models import Contacts, Product


def index(request):
    products = Product.objects.all()
    # products = Product.objects.all().order_by('-id')[:5]
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
