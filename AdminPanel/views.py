import statistics
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from AdminPanel.models import Registration

# Create your views here.

# def verification(request):
#     return render(request, "AdminPanel/otp-verification.html")


def dashboard(request):
    return render(request, "AdminPanel/home.html")


def registration(request):

    query_results = Registration.objects.all()
    print(query_results)
    

    if request.method == "POST":
        fname=request.POST.get("fname")
        lname=request.POST.get('lname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        dreams=request.POST.get('dreams')
        dreamsOption=request.POST.getlist('dreamsOption')
        # print(dreamsOption)
        en=Registration.objects.create(fname=fname,lname=lname,phone=phone,email=email,dreams=dreams,dreamsOption=dreamsOption)
        # print(en)
        en.save()
        
        return render(request,"AdminPanel/registration.html",{'query_results':query_results})
        # return redirect("registration")
    else:
        return render(request, "AdminPanel/registration.html",{'query_results':query_results})


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

        else:
            return redirect("signup")


    else :
        return render(request,'AdminPanel/login.html')


        

