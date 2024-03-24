from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("bookings/", include("bookings.urls"), name="bookings-urls"),
    path("library/", include("library.urls"), name="library-urls"),
    path("", include("events.urls"), name="events-urls"),
    path('summernote/', include('django_summernote.urls')),
]
