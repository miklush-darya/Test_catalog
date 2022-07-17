from django import forms
from .models import *

# class AddProdForm(forms.Form):

#     title = forms.CharField(max_length=255, label='Продукт')
#     slug = forms.SlugField(max_length=255, label='URL')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}), label='Описание')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
#     categ = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
#     # photo = models.ImageField(upload_to='photos/%Y/%m/')


class AddProdForm(forms.ModelForm):

    # title = forms.CharField(max_length=255, label='Продукт')
    # slug = forms.SlugField(max_length=255, label='URL')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}), label='Описание')
    # is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
    # categ = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    
    class Meta:
        model = Catalog
        fields = ['title', 
                    'slug', 
                    'content', 
                    'is_published', 
                    'categ'
                ]