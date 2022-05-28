from django.contrib import admin
from django.urls import path, include

from research.views import publications, research

urlpatterns = [
    path('', research, name='research'),
    path('publications', publications, name='publications'),
]
