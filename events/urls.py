from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:event_id>/', views.event_detail, name="event_detail"),
    path('events/<int:event_id>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
]