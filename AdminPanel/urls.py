from django.urls import path, include

<<<<<<< HEAD
from AdminPanel.views import dashboard, head, registration, signup, verification, view_dt
=======
from AdminPanel.views import country, dashboard, events, registration, reports, signup, verification, view_dt
>>>>>>> 9a72e22fc0d0cdc5d7530418bd4c96d8ba516126

urlpatterns = [
    path('signup',signup,name="signup"),
    path('verification',verification,name="verification"),
    path('dashboard',dashboard,name="dashboard"),
    path('registration',registration,name="registration"),
    path('view_dt',view_dt,name="view-dt"),
<<<<<<< HEAD
    path('head',head,name="head"),
=======
    path('reports',reports,name="reports"),
    path('events',events,name="events"),
    path('country',country,name="country"),
>>>>>>> 9a72e22fc0d0cdc5d7530418bd4c96d8ba516126
]
