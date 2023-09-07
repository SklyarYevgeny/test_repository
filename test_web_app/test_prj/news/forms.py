from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForms(ModelForm):
    class Meta:
        model = Articles
        fields = [
            'name',
            'anons',
            'full_text',
            'data'
        ]
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи:',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи:',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи:',
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата статьи:',
            })
        }
