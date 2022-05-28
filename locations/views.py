from django.shortcuts import render


# Create your views here.
def locations(request,loc):
    if loc == 'bangalore':
        return render(request, 'location/bangalore.html')
