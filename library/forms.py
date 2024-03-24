from django import forms
from .models import BoardGame


class SearchForm(forms.Form):
    query = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search games',
                'class': 'form-control mr-sm-2',
                'aria-label': 'Search'
            }
        ),
        label=''
    )
