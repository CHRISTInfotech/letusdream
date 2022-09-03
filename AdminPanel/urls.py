from django.urls import path, include

from AdminPanel.views import dashboard, registration, signup, verification, view_dt

urlpatterns = [
    path('signup',signup,name="signup"),
    path('verification',verification,name="verification"),
    path('dashboard',dashboard,name="dashboard"),
    path('registration',registration,name="registration"),
    path('view_dt',view_dt,name="view-dt"),
]
