from django import forms
from .models import BoardGame


class SearchForm(forms.Form):
    """
    A form for searching board games.
    
    **Fields**
    
    ``query``
        A text input field for entering the search term.
    """
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
