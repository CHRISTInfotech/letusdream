from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    return render(request, 'Admin/login.html')


def verification(request):
    return render(request, "Admin/otp-verification.html")


def dashboard(request):
    return render(request, "Admin/home.html")


def registration(request):
    return render(request, "Admin/registration.html")


def view_dt(request):

    return render(request, "Admin/view-dt.html")


def reports(request):
    return render(request, "Admin/reports.html")


def events(request):
    return render(request, "Admin/events.html")
