from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


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
    attendees = models.ManyToManyField(
        User, blank=True, related_name='event_attendees')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return f"{self.name} on {self.event_date} at {self.event_time}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`events.Event`.
    """
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, blank=True, related_name='comment_likes')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
