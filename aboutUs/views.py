from django.shortcuts import render


# Create your views here.
def aboutUs(request):
    return render(request, 'aboutUs/aboutUs.html')


def aboutusMedia(request):
    return render(request, 'aboutUs/aboutusMedia.html')
