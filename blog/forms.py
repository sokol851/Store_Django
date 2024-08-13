from django import forms

from catalog.forms import StyleFormMixin
from blog.models import Blog


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'content', 'preview', 'is_published')
