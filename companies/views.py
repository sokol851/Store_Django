from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from companies.models import Companies


class CompaniesCreateView(CreateView):
    model = Companies
    fields = ('title', 'description',)
    success_url = reverse_lazy('companies:list')

    def form_valid(self, form):
        if form.is_valid():
            new_company = form.save()
            new_company.slug = slugify(new_company.title)
            new_company.save()

        return super().form_valid(form)


class CompaniesListView(ListView):
    model = Companies

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class CompaniesDetailView(DetailView):
    model = Companies

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class CompaniesUpdateView(UpdateView):
    model = Companies
    fields = ('title', 'description',)

    def form_valid(self, form):
        if form.is_valid():
            new_company = form.save()
            new_company.slug = slugify(new_company.title)
            new_company.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('companies:view', args=[self.kwargs.get('pk')])


class CompaniesDeleteView(DeleteView):
    model = Companies
    success_url = reverse_lazy('companies:list')
