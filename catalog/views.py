from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from .models import Contacts, Product, Feedback, Blog


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
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        if form.is_valid():
            new_prod = form.save()
            new_prod.slug = slugify(new_prod.name)
            new_prod.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
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


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:list_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'preview', 'is_published')
    slug_url_kwarg = 'the_slug_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail_blog', args=[self.kwargs.get('the_slug_blog')])


class BlogDeleteView(DeleteView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'
    success_url = reverse_lazy('catalog:list_blog')
