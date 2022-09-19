import statistics
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    return render(request, 'AdminPanel/login.html')


def verification(request):
    return render(request, "AdminPanel/otp-verification.html")


def dashboard(request):
    return render(request, "AdminPanel/home.html")


def registration(request):
    return render(request, "AdminPanel/registration.html")


def view_dt(request):

    return render(request, "AdminPanel/view-dt.html")


def reports(request):
    return render(request, "AdminPanel/reports.html")


def events(request):
    return render(request, "AdminPanel/events.html")


def modify_statistics(request):
    return render(request, "AdminPanel/modify-statistics.html")
