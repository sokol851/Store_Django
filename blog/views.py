from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'

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
        return reverse('blog:detail_blog', args=[self.kwargs.get('the_slug_blog')])

    @staticmethod
    def toggle_activity(request, pk):
        product_items = get_object_or_404(Blog, pk=pk)
        if product_items.is_published:
            product_items.is_published = False
        else:
            product_items.is_published = True

        product_items.save()
        return redirect(reverse('blog:list_blog'))


class BlogDeleteView(DeleteView):
    model = Blog
    slug_url_kwarg = 'the_slug_blog'
    success_url = reverse_lazy('blog:list_blog')
