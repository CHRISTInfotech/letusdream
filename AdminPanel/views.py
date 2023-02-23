import statistics
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from AdminPanel.models import Registration
from home.models import ConferenceRegistration

# Create your views here.

# def verification(request):
#     return render(request, "AdminPanel/otp-verification.html")

@login_required
def dashboard(request):
    r1 = ConferenceRegistration.objects.filter(user_type='Paticipant').all()
    r2 = ConferenceRegistration.objects.filter(user_type='Volunteer').all()
    r3 = ConferenceRegistration.objects.filter(user_type='Partner').all()
    return render(request, "AdminPanel/home.html",{'r1':r1,'r2':r2,'r3':r3})


def registration(request):
    # query_results = ConferenceRegistration.objects.all()
    query_results = ConferenceRegistration.objects.filter(user_type='Paticipant').values()
    r2 = ConferenceRegistration.objects.filter(user_type='Volunteer').values()
    r3 = ConferenceRegistration.objects.filter(user_type='Partner').values()
    # print(query_results)
    return render(request, "AdminPanel/registration.html",{'query_results':query_results,'r2':r2,'r3':r3})

# def login(request):
#     if request.method == "POST":
#         r1 = ConferenceRegistration.objects.filter(user_type='Paticipant').all()
#         print(r1)
#         return render(request, "AdminPanel/home.html",{'r1':r1})

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
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
        
            if user is not None:
                login(request, user)
                # return HttpResponseRedirect('/AdminPanel/verification/')
                print("Login Success")
                return redirect("dashboard")

        else:
            print("Login Fail")
            return redirect("signup")
            # return render(request, "AdminPanel/home.html")


    else :
        return render(request,'AdminPanel/login.html')

def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.")
    return redirect("signup")
        

