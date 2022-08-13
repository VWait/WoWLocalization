from .models import SimpleSearchRequest
from django.forms import ModelForm, TextInput


class SearchForm(ModelForm):
    class Meta:
        model = SimpleSearchRequest
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Название карты'
            })
        }
