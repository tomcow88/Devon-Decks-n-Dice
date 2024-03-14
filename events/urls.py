from . import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<int:event_id>/', views.event_detail, name="event_detail"),
]