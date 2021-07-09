from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'author', 'language', 'genre']