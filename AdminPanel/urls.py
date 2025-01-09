from django.urls import path, include

from AdminPanel.views import  email_subscription


urlpatterns = [
    path('subscribe-email',email_subscription,name='subscribe-email')
]

