from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['email', 'party_size', 'session_length', 'start_time', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }