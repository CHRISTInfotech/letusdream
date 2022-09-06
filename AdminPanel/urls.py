from django.urls import path, include

from AdminPanel.views import country, dashboard, events, registration, reports, signup, verification, view_dt

urlpatterns = [
    path('signup',signup,name="signup"),
    path('verification',verification,name="verification"),
    path('dashboard',dashboard,name="dashboard"),
    path('registration',registration,name="registration"),
    path('view_dt',view_dt,name="view-dt"),
    path('reports',reports,name="reports"),
    path('events',events,name="events"),
    path('country',country,name="country"),
]
