from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def aboutUs(request):
    return render(request, 'aboutUs/aboutUs.html')


def media(request):
    return render(request, 'aboutUs/media.html')


def pressRelease(request):
    return render(request, 'aboutUs/media-view-photo.html')


def newsletter(request):
    return render(request, 'aboutUs/newsletter.html')


def photoGallery(request):
    return render(request, 'aboutUs/photo-gallery.html')


def aboutConference(request):
    return render(request, 'conference/aboutConference.html')


def annualConference(request):
    return render(request, 'conference/annual-conference.html')


def trriennialConference(request):
    return render(request, 'conference/triennialConference.html')


def bangalorechristuniversity(request):
    return render(request, 'conference/christ-university-bangalore.html')


def binghamtonUniversity(request):
    return render(request, 'conference/binghamton-university.html')


def cuT(request):
    return render(request, 'conference/cuT.html')


def jncaB(request):
    return render(request, 'conference/jncaB.html')


def louisianatechuniversity(request):
    return render(request, 'conference/louisiana-tech-university.html')


def yclpCourse(request):
    return render(request, 'courses/yclpCourse.html')


def dreams(request, drm):
    if drm == 'band':
        return render(request, 'dreams/dreamsBand.html', {'drm': drm})
    elif drm == 'proclub':
        return render(request, 'dreams/dreamsProclub.html', {'drm': drm})
    elif drm == 'program':
        return render(request, 'dreams/dreamsProgram.html', {'drm': drm})
    elif drm == 'leadershipnetwork':
        return render(request, 'dreams/leadershipNetwork.html', {'drm': drm})


def locations(request, loc):
    if loc == 'bangalore':
        return render(request, 'location/india/bangalore.html')
    elif loc == 'changancherry':
        return render(request, 'location/india/changancherry.html')
    elif loc == 'mannanam':
        return render(request, 'location/india/mannanam.html')
    elif loc == 'thiruvallam':
        return render(request, 'location/india/thiruvallam.html')
    elif loc == 'thiruvananthapuram':
        return render(request, 'location/india/thiruvananthapuram.html')
    elif loc == 'cologne':
        return render(request, 'location/germany/cologne.html')
    elif loc == 'bastrope':
        return render(request, 'location/usa/bastrope.html')
    elif loc == 'dalias':
        return render(request, 'location/usa/dalias.html')
    elif loc == 'lagrande':
        return render(request, 'location/usa/lagrande.html')
    elif loc == 'mcallen':
        return render(request, 'location/usa/mcallen.html')
    elif loc == 'monroe':
        return render(request, 'location/usa/monroe.html')


def research(request):
    return render(request, 'research/research.html')


def publications(request):
    return render(request, 'research/publications.html')


def registration_user(request):
   return render(request, 'registration.html')

def calender(request):
    return render(request,'home/calender.html')
