from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Event(models.Model):
    """
    Stores a single event entry related to :model:`auth.User`
    """
    name = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    event_date = models.DateField()
    event_time = models.TimeField()
    max_attendees = models.IntegerField()
    attendees = models.ManyToManyField(User)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return f"{self.name} on {self.event_date}"