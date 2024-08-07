from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, SubjectForm
from catalog.models import Contacts, Product, Feedback, Subject


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST)
        else:
            context_data['formset'] = SubjectFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid():
            self.object.slug = slugify(self.object.name)
            self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    slug_url_kwarg = 'the_slug_prod'

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if form.is_valid():
            self.object.slug = slugify(self.object.name)
            self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

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
