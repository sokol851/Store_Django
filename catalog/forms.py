from django import forms

from catalog.models import Product, Subject


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'preview', 'category', 'price',)
        # exclude = ('is_active',)

    def clean_name(self):
        clean_data = self.cleaned_data['name']
        list_stop_word = ['казино', 'заработай']
        for i in list_stop_word:
            if i in clean_data:
                raise forms.ValidationError('Данный товар запрещён к продаже')
        return clean_data


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
