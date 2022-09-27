import statistics
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.

# def verification(request):
#     return render(request, "AdminPanel/otp-verification.html")


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


#Login view function

def signup(request):
    if request.method == "POST":
       username=request.POST['username']
       password=request.POST['password']

       user=authenticate(request,username=username,password=password)
      
       if user is not None:
        login(request,user)
        # return HttpResponseRedirect('/AdminPanel/verification/')
        return redirect("dashboard")

    else :
        return render(request,'AdminPanel/login.html')

