from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_current':
                field.widget.attrs['class'] = 'form-check-input'


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
