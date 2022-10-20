import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.models import ConferenceRegistration


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

def donboscocollege(request):
    return render(request,'conference/donbosco-college-of-arts-and-science.html')

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
    elif loc == 'chennai':
        return render(request, 'location/india/chennai.html')
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

    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        aboutme=request.POST.get('aboutme')
        aboutother=request.POST.get('aboutother')
        orgaff=request.POST.get('orgaff')
        orgname=request.POST.get('orgname')
        phone=request.POST.get('phone')
        confdate=request.POST.getlist('confdate')
        prevconf=request.POST.getlist('prevconf')

        confreg=ConferenceRegistration.objects.create(name=name,email=email,aboutme=aboutme,aboutother=aboutother,orgaff=orgaff,orgname=orgname,phone=phone,confdate=confdate,prevconf=prevconf)
        confreg.save()
        print(confreg)
        return redirect('registration_user')
    else :
        return render(request,'registration.html')
#    return render(request, 'registration.html')

def calender(request):
    return render(request,'home/calender.html')

def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')    
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    confreg = ConferenceRegistration.objects.all()  
    writer = csv.writer(response)  

    writer.writerow(['Name','Email ID','About me','if other','Organisation Affilation','Organisation Name','Phone No','Conference Date','Previous Conference'])
    for i in confreg:
        writer.writerow([i.name,i.email,i.aboutme,i.aboutother,i.orgaff,i.orgname,i.phone,i.confdate,i.prevconf])
    return response

def testimonials(request):
    return render(request,'home/view_testimonials.html')
