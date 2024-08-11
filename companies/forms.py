from django import forms

from catalog.forms import StyleFormMixin
from companies.models import Companies


class CompaniesForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Companies
        fields = ('title', 'description',)
