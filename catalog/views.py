from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm
from catalog.models import Contacts, Product, Feedback


class ProductListView(ListView):
    model = Product


class ContactsListView(ListView):
    model = Contacts


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('name', 'email', 'content')
    success_url = reverse_lazy('catalog:list_feedback')


class FeedbackListView(ListView):
    model = Feedback


class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'the_slug_prod'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        if form.is_valid():
            new_prod = form.save()
            new_prod.slug = slugify(new_prod.name)
            new_prod.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    slug_url_kwarg = 'the_slug_prod'

    def form_valid(self, form):
        if form.is_valid():
            new_prod = form.save()
            new_prod.slug = slugify(new_prod.name)
            new_prod.save()
        return super().form_valid(form)

    @staticmethod
    def toggle_activity(request, pk):
        product_items = get_object_or_404(Product, pk=pk)
        if product_items.is_active:
            product_items.is_active = False
        else:
            product_items.is_active = True

        product_items.save()
        return redirect(reverse('catalog:index'))


class ProductDeleteView(DeleteView):
    model = Product
    slug_url_kwarg = 'the_slug_prod'
    success_url = reverse_lazy('catalog:index')
