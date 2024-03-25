from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .forms import CommentForm
from .models import Event, Comment


def home(request):
    return render(request, "index.html")


class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1)
    template_name = "events/event_list.html"
    paginate_by = 6


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = event.comments.all().order_by("-created_on")
    comment_count = event.comments.filter(approved=True).count()
    attendees_count = event.attendees.all().count()

    attending = event.attendees.filter(id=request.user.id).exists()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.event = event
            comment_form.save()
            messages.success(
                request, 'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(
                reverse('event_detail', args=[event_id])
            )

    else:
        comment_form = CommentForm()

    return render(request, "events/event_detail.html", {
        "event": event,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "attendees_count": attendees_count,
        "attending": attending,
    })


def comment_edit(request, event_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Comment Updated!')
            return HttpResponseRedirect(
                reverse('event_detail', args=[event_id])
            )
        else:
            messages.error(request, 'Error updating comment!')
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))


def comment_delete(request, event_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))


def AttendView(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.attendees.filter(id=request.user.id).exists():
        event.attendees.remove(request.user)
    else:
        event.attendees.add(request.user)
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
