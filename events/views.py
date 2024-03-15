from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event

# Create your views here.


class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "events/event_list.html"
    paginate_by = 6


def event_detail(request, event_id):
    """
    Display an individual :model:`events.Event`.

    **Context**

    ``event``
        An instance of :model:`events.Event`.

    **Template:**

    :template:`events/event_detail.html`
    """
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, id=event_id)
    comments = event.comments.all().order_by("-created_on")
    comment_count = event.comments.filter(approved=True).count()
    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "comments": comments,
            "comment_count": comment_count,
        },
    )