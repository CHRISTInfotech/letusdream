from django.shortcuts import render


# Create your views here.
def aboutConference(request):
    return render(request, 'conference/aboutConference.html')


def buNY(request):
    return render(request, 'conference/buNY.html')


def cuB(request):
    return render(request, 'conference/cuB.html')


def cuT(request):
    return render(request, 'conference/cuT.html')


def jncaB(request):
    return render(request, 'conference/jncaB.html')


def ltuLouisiana(request):
    return render(request, 'conference/luLouisiana.html')
