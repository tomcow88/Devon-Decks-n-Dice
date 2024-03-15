from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .models import Table, Booking
from .forms import BookingForm


# Create your views here.

def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            try:
                booking = booking_form.save(commit=False)
                booking.name = request.user
                booking.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your booking was created successfully!'
                )
                return redirect('bookings')
            except ValidationError as e:
                messages.error(request, e.message)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please try again.')

    booking_form = BookingForm()
    
    return render(
        request,
        'bookings/booking_form.html',
        {'booking_form': booking_form}
    )