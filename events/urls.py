from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:event_id>/', views.event_detail, name="event_detail"),
    path('events/<int:event_id>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('events/<int:event_id>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('attend/<int:event_id>', views.AttendView, name='attend_event'),
]