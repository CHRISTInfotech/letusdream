from django.urls import path, include

from AdminPanel.views import  dashboard, events, modify_statistics, registration, reports, signup, view_dt, logout_request


urlpatterns = [
    path('signup',signup,name="signup"),
    # path('verification',verification,name="verification"),
    path('dashboard',dashboard,name="dashboard"),
    path('registration',registration,name="registration"),
    path('view_dt',view_dt,name="view-dt"),
    path('reports',reports,name="reports"),
    path('events',events,name="events"),
    path('modify_statistics',modify_statistics,name="modify_statistics"),
    path('logout', logout_request, name="logout"),
    
]

