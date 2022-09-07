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
<<<<<<< HEAD
    return render(request, "Admin/view-dt.html")


def head(request):
    return render(request, 'head.html')
=======
    return render(request,"Admin/view-dt.html")

def reports(request):
    return render(request,"Admin/reports.html")

def events(request):
    return render(request,"Admin/events.html")

def country(request):
    return render(request,"Admin/country.html")
>>>>>>> 9a72e22fc0d0cdc5d7530418bd4c96d8ba516126
