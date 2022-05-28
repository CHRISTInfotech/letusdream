from django.contrib import admin
from django.urls import path, include

from locations.views import locations

urlpatterns = [
    path('locations/<str:loc>', locations, name='location'),
]
