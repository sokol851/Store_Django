from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version, Feedback


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    list_stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                      'радар']

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'preview', 'category', 'price',)
        # exclude = ('is_active',)

    def clean_name(self):
        clean_data = self.cleaned_data['name']

        for word in self.list_stop_word:
            if word.lower() in clean_data.lower():
                raise forms.ValidationError('Данный товар запрещён к продаже')
        return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data['description']

        for word in self.list_stop_word:
            if word.lower() in clean_data.lower():
                raise forms.ValidationError('Данный товар запрещён к продаже')
        return clean_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class FeedbackForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'content')


class ProdModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "description", "is_active",)
