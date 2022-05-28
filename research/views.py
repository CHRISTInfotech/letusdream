from django.shortcuts import render


# Create your views here.
def publications(request):
    return render(request, 'research/publications.html')


def research(request):
    return render(request, 'research/research.html')
