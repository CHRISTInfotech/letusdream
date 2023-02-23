import statistics
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login

# from AdminPanel.models import Registration
from home.models import ConferenceRegistration

# Create your views here.

# def verification(request):
#     return render(request, "AdminPanel/otp-verification.html")


def dashboard(request):
    return render(request, "AdminPanel/home.html")


def registration(request):
    # query_results = ConferenceRegistration.objects.all()
    query_results = ConferenceRegistration.objects.filter(user_type='Paticipant').values()
    r2 = ConferenceRegistration.objects.filter(user_type='Volunteer').values()
    r3 = ConferenceRegistration.objects.filter(user_type='Partner').values()
    # print(query_results)
    return render(request, "AdminPanel/registration.html",{'query_results':query_results,'r2':r2,'r3':r3})

def login(request):
    if request.method == "POST":
        r1 = ConferenceRegistration.objects.all()
        return render(request, "AdminPanel/home.html",{'query_results':r1})

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
            return HttpResponseRedirect('/AdminPanel/verification/')
            return redirect("dashboard")

        else:
            # return redirect("signup")
            return render(request, "AdminPanel/home.html")


    else :
        return render(request,'AdminPanel/login.html')


        

