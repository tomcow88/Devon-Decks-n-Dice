from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Comment
from .forms import CommentForm

# Create your views here.


class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
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
    attendees_count = event.attendees.all().count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "attendees_count": attendees_count,
        },
    )

def comment_edit(request, event_id, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, id=event_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))

def comment_delete(request, event_id, comment_id):
    """
    view to delete comment
    """
    queryset = Event.objects.filter(status=1)
    post = get_object_or_404(queryset, id=event_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))

def AttendView(request, event_id):
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    event.attendees.add(request.user)
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))