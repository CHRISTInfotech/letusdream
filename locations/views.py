from django.shortcuts import render


# Create your views here.
def bangalore(request):
    return render(request, 'location/bangalore.html')


def bastrope(request):
    return render(request, 'location/bastrope.html')


def changancherry(request):
    return render(request, 'location/changancherry.html')


def cologne(request):
    return render(request, 'location/cologne.html')


def dalias(request):
    return render(request, 'location/dalias.html')


def lagrande(request):
    return render(request, 'location/lagrande.html')


def mannanam(request):
    return render(request, 'location/mannanam.html')


def mcallen(request):
    return render(request, 'location/mcallen.html')


def monroe(request):
    return render(request, 'location/monroe.html')

def thiruvallam(request):
    return render(request, 'location/thiruvallam.html')

def thiruvananthapuram(request):
    return render(request, 'location/thiruvananthapuram.html')
