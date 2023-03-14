import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.models import ConferenceRegistration


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def aboutUs(request):
    return render(request, 'aboutUs/aboutUs.html')

def login(request):
    if request.method == "POST":
        return render(request, "AdminPanel/home.html")
    
def media(request):
    return render(request, 'aboutUs/media.html')


def pressRelease(request):
    return render(request, 'aboutUs/media-view-photo.html')


def newsletter(request):
    return render(request, 'aboutUs/newsletter.html')


def photoGallery(request):
    return render(request, 'aboutUs/photo-gallery.html')


def youtubeMedia(request):
    return render(request, 'aboutUs/media-yt.html')


def aboutConference(request):
    return render(request, 'conference/aboutConference.html')


def allConferences(request):
    return render(request, 'conference/annualConference.html')


def triennialConference(request):
    return render(request, 'conference/triennialConference.html')

def triennialConference2020(request):
    return render(request, 'conference/triennialConference/triennialConference2020.html')

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
    return render(request, 'conference/donbosco-college-of-arts-and-science.html')


def stannescollege(request):
    return render(request, 'conference/stannes-college.html')


def loyolacollegeConference(request):
    return render(request, 'conference/loyola.html')


def universityofLouisianaMonroe(request):
    return render(request, 'conference/universityofLouisianaMonroe.html')


def allsaintssollege(request):
    return render(request, 'conference/allsaintssollege.html')


def louisianastateuniversityshreveport(request):
    return render(request, 'conference/louisianastateuniversityshreveport.html')


def gramblingstateuniversitylouisiana(request):
    return render(request, 'conference/grambling-state-university-louisiana.html')


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
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inter = request.POST.get('inter')
        utype = request.POST.get('utype')
        staddr = request.POST.get('staddr')
        # stphone = request.POST.get('st_phone')
        stgrade = request.POST.get('stgrade')
        ptname = request.POST.get('ptname')
        ptphone = request.POST.get('ptphone')
        ptemail = request.POST.get('ptemail')
        ptaddr = request.POST.get('ptaddr')
        volt = request.POST.get('volt')
        intro = request.POST.get('intro')
        expertise = request.POST.get('expertise')
        # vlphone = request.POST.get('vl_phone')
        partaddr = request.POST.get('partaddr')
        # partphone= request.POST.get('ptr_phone')
        partmsg = request.POST.get('partmsg')

        confreg = ConferenceRegistration.objects.create(
        name = name ,
        email = email , 
        phone = phone , 
        interest = inter , 
        user_type = utype , 
        st_addr = staddr , 
        # st_phone = stphone , 
        st_grade = stgrade , 
        st_Pname = ptname , 
        st_Pnum = ptphone , 
        st_Pemail = ptemail , 
        st_Paddr = ptaddr , 
        vl_type = volt , 
        vl_about = intro , 
        vl_expert = expertise , 
        # vl_phone = vlphone , 
        ptr_addr = partaddr , 
        # ptr_phone= partphone , 
        ptr_msg = partmsg)
        confreg.save()
        print(confreg)
        return redirect('registration_user')
    else:
        print("Failed")
        return render(request, 'registration.html')
#    return render(request, 'registration.html')


def calender(request):
    return render(request, 'home/calender.html')


def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="participant_list.csv"'
    confreg = ConferenceRegistration.objects.filter(user_type='Paticipant').all()
    # confreg = ConferenceRegistration.objects.all()

    print(confreg)
    writer = csv.writer(response)

    writer.writerow(['Date','Name', 'Email ID', 'Phone No', 'Interest', 'Student Address',
                    'Student Grade', 'Parent Name', 'Parent Mobile', 'Parent Email ID',
                    'Parent Address', 'User Type'])
    for i in confreg:
        writer.writerow([i.date, i.name, i.email, i.phone, i.interest, i.st_addr, i.st_grade,
                         i.st_Pname, i.st_Pnum, i.st_Pemail, i.st_Paddr, i.user_type])
    return response

def downloadvoltcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vounteer_list.csv"'
    confreg = ConferenceRegistration.objects.filter(user_type='Volunteer').all()

    writer = csv.writer(response)

    writer.writerow(['Date', 'Name', 'Email ID', 'Phone No', 'Interest', 'Volunteer Type',
                    'Intro', 'Areas of expertise',  'User Type'])
    for i in confreg:
        writer.writerow([i.date, i.name, i.email, i.phone, i.interest, i.vl_type,
                         i.vl_about, i.vl_expert, i.user_type])
    return response

def downloadpartcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="partner_list.csv"'
    confreg = ConferenceRegistration.objects.filter(user_type='Partner').all()

    writer = csv.writer(response)

    writer.writerow(['Date', 'Name', 'Email ID', 'Phone No', 'Interest', 'Address',
                    'Message', 'User Type'])
    for i in confreg:
        writer.writerow([i.date, i.name, i.email, i.phone, i.interest, i.ptr_addr, i.ptr_msg, i.user_type])
    return response

def testimonials(request):
    return render(request, 'home/view_testimonials.html')
