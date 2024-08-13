from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, FeedbackForm
from catalog.models import Contacts, Product, Feedback, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_list = Product.objects.all()
        context_data['product_versions'] = {}
        for product in product_list:
            if len(product.versions.filter(is_current=True)):
                version = product.versions.filter(is_current=True).last()
                context_data['product_versions'].update({product: version})
        return context_data

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset


class ContactsListView(ListView):
    model = Contacts


class FeedbackCreateView(CreateView):
    model = Feedback
    success_url = reverse_lazy('catalog:list_feedback')
    form_class = FeedbackForm


class FeedbackListView(ListView):
    model = Feedback


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    slug_url_kwarg = 'the_slug_prod'
    login_url = 'users:login'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        if form.is_valid():
            self.object.slug = slugify(self.object.name)
            self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    slug_url_kwarg = 'the_slug_prod'
    login_url = 'users:login'

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        counter = 0
        self.object.slug = slugify(self.object.name)

        for form_version in formset:
            if form_version.is_valid():
                if form_version.cleaned_data.get('is_current'):
                    counter += 1

        if counter > 1:
            form.add_error(None, ValidationError('Только одна версия товара может быть активной'))
            return self.form_invalid(form)

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        context_data = self.get_context_data()
        context_data['form'] = form
        return self.render_to_response(context_data)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    slug_url_kwarg = 'the_slug_prod'
    success_url = reverse_lazy('catalog:index')
    login_url = 'users:login'
