from django.shortcuts import render


# Create your views here.
def dreamsBand(request):
    return render(request, 'dreams/dreamsBand.html')


def dreamsBand(request):
    return render(request, 'dreams/dreamsProclub.html')


def dreamsProgram(request):
    return render(request, 'dreams/dreamsProgram.html')


def leadershipNetwork(request):
    return render(request, 'dreams/leadershipNetwrok.html')

