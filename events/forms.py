from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)
