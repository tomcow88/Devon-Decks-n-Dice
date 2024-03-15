from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_booking, name='create_booking'),
]