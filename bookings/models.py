from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

TIME_CHOICES = (
    ("10:00", "10 AM"),
    ("11:00", "11 AM"),
    ("12:00", "12 PM"),
    ("13:00", "1 PM"),
    ("14:00", "2 PM"),
    ("15:00", "3 PM"),
    ("16:00", "4 PM"),
    ("17:00", "5 PM"),
    ("18:00", "6 PM"),
    ("19:00", "7 PM"),
    ("20:00", "8 PM"),
)

SESSION_LENGTH_CHOICES = (
    (2, '2 hours'),
    (4, '4 hours'),
)

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}, Capacity: {self.capacity}"

class Booking(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    email = models.EmailField()
    party_size = models.IntegerField()
    session_length = models.IntegerField(choices=SESSION_LENGTH_CHOICES)
    start_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    end_time = models.TimeField(null=True)
    date = models.DateField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="bookings")

    def calculate_end_time(self):
        start_datetime = datetime.datetime.strptime(self.start_time, '%H:%M')
        end_datetime = start_datetime + datetime.timedelta(hours=self.session_length)
        return end_datetime.time()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.end_time = self.calculate_end_time()
            self.table = self.find_available_table()
        super(Booking, self).save(*args, **kwargs)

    def find_available_table(self):
        end_time = self.calculate_end_time()
        available_tables = Table.objects.filter(capacity__gte=self.party_size).exclude(
            bookings__date=self.date,
            bookings__start_time__lte=end_time.strftime('%H:%M'),
            bookings__end_time__gte=self.start_time
        ).order_by('capacity')
        if available_tables:
            return available_tables.first()
        else:
            raise ValidationError("No available tables for the selected time and party size.")