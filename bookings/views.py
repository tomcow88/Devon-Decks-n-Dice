from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.views import generic
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
                duplicate_bookings = Booking.objects.filter(
                    name=request.user, date=booking.date)
                if duplicate_bookings.exists():
                    messages.error(
                        request,
                        'You have already booked a table on this date. '
                        'If you want to ammend your booking, please get '
                        'in touch.'
                    )
                    return render(request, 'bookings/booking_form.html',
                                  {'booking_form': booking_form})
                booking.clean()
                booking.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your booking was created successfully!'
                )
                return redirect('bookings')
            except ValidationError as e:
                if hasattr(e, 'message_dict'):
                    for field, messages_list in e.message_dict.items():
                        for message in messages_list:
                            messages.error(request, message)
                else:
                    for message in e.messages:
                        messages.error(request, message)
        else:
            for field, errors in booking_form.errors.items():
                for error in errors:
                    messages.error(request, error)

    booking_form = BookingForm()

    return render(
        request,
        'bookings/booking_form.html',
        {'booking_form': booking_form}
    )
