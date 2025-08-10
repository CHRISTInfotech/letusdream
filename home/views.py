import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .location_data import locations_data
from .testimonials_data import TESTIMONIALS_DATA
from .conference import CONFERENCE_DATA
from .llfp_2024 import llfp_2024


def index(request):
    context = {
       'page_title': 'Home',
    }
    return render(request, 'home/index.html')


def aboutUs(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Overview', 'url': None, 'icon': 'fas fa-eye', 'active': True}
    ]
    return render(request, 'aboutUs/aboutUs.html', {'breadcrumbs': breadcrumbs})


def leadership(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Leadership', 'url': None, 'icon': 'fas fa-user-tie', 'active': True}
    ]
    return render(request, "aboutUs/leadership.html", {'breadcrumbs': breadcrumbs})


def login(request):
    if request.method == "POST" and request.user.is_authenticated:
        return render(request, "AdminPanel/home.html")


def media(request):
    breadcrumbs = [
    {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
    {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
    {'name': 'Media', 'url': None, 'icon': 'fas fa-photo-video', 'active': True}
]

    return render(request, 'aboutUs/media.html', {'breadcrumbs': breadcrumbs})


def events(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Events', 'url': None, 'icon': 'fas fa-calendar-days', 'active': True}
    ]

    return render(request, 'aboutUs/events.html', {'breadcrumbs': breadcrumbs})


def pressRelease(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Press Release', 'url': None, 'icon': 'fas fa-newspaper', 'active': True}
    ]
    return render(request, 'aboutUs/media-view-photo.html', {'breadcrumbs': breadcrumbs})


def newsletter(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Newsletter', 'url': None, 'icon': 'fas fa-envelope', 'active': True}
    ]
    return render(request, 'aboutUs/newsletter.html', {'breadcrumbs': breadcrumbs})


def photoGallery(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Photo Gallery', 'url': None, 'icon': 'fas fa-image', 'active': True}
    ]
    return render(request, 'aboutUs/photo-gallery.html', {'breadcrumbs': breadcrumbs})


def youtubeMedia(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'YouTube Media', 'url': None, 'icon': 'fab fa-youtube', 'active': True}
    ]
    return render(request, 'aboutUs/media-yt.html', {'breadcrumbs': breadcrumbs})


def aboutConference(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'Conference', 'url': None, 'icon': 'fas fa-calendar', 'active': False},
        {'name': 'About Conference', 'url': None, 'icon': 'fas fa-info-circle', 'active': True}
    ]
    return render(request, 'conference/aboutConference.html', {'breadcrumbs': breadcrumbs})


def allConferences(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'Conference', 'url': None, 'icon': 'fas fa-calendar', 'active': False},
        {'name': 'Annual Conferences', 'url': None, 'icon': 'fas fa-calendar-alt', 'active': True}
    ]
    return render(request, 'conference/annualConference.html', {'breadcrumbs': breadcrumbs})


def triennialConference(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'Conference', 'url': 'Conferences', 'icon': 'fas fa-calendar', 'active': False},
        {'name': 'Triennial Conferences', 'url': None, 'icon': 'fas fa-calendar-alt', 'active': True}
    ]
    return render(request, 'conference/triennialConference.html', {'breadcrumbs': breadcrumbs,})


def triennialConference2020(request):
    breadcrumbs = [
    {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
    {'name': 'Conferences', 'url': None, 'icon': 'fas fa-calendar-alt', 'active': False},
    {'name': 'Triennial Conferences', 'url': 'trriennial-conference', 'icon': 'fas fa-calendar-check', 'active': False},
    {'name': '2020 Conference', 'url': None, 'icon': 'fas fa-file-alt', 'active': True}
]

    return render(request, 'conference/triennialConference/triennialConference2020.html', {'breadcrumbs': breadcrumbs,})


def triennialConference2023(request):
    breadcrumbs = [
    {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
    {'name': 'Conferences', 'url': None, 'icon': 'fas fa-calendar-alt', 'active': False},
    {'name': 'Triennial Conferences', 'url': 'trriennial-conference', 'icon': 'fas fa-calendar-check', 'active': False},
    {'name': '2023', 'url': None, 'icon': 'fas fa-file-alt', 'active': True}
]

    context = {
        'bgcolor': '#274C7D',
        "conference_data": CONFERENCE_DATA,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'conference/triennialConference/triennialConference2023.html', context)

def howtoConference(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'Conference', 'url': None, 'icon': 'fas fa-calendar-alt', 'active': False},
        {'name': 'Conference Resources', 'url': None, 'icon': 'fas fa-box-open', 'active': True}
    ]
    return render(request,'conference/ludConferences.html', {'breadcrumbs': breadcrumbs,})

def annualConferences(request, year, location):
    if int(year) == 2024 and location == "stfrancisdesalescollege":
        return render(request,"conference/annualConference/2024/stfrancisdesalescollege.html")
    elif int(year) == 2024 and location == "womenschristiancollege":
        return render(request,"conference/annualConference/2024/womenschristiancollege.html")
    elif int(year) == 2024 and location == "gramblingstateuniversity":
        return render(request,"conference/annualConference/2024/gamblingstateuniversity.html")
    elif int(year) == 2024 and location == "binghamtonuniversity2024":
        return render(request,"conference/annualConference/2024/binghamtonuniversity2024.html")
    elif int(year) == 2024 and location == "christnagarcollege":
        return render(request,"conference/annualConference/2024/christnagarcollege.html")
    elif int(year) == 2024 and location == "stfrancisdegreecollege":
        return render(request,"conference/annualConference/2024/stfrancisdegreecollege.html")
    elif int(year) == 2024 and location == "savitribaiphulepune":
        return render(request,"conference/annualConference/2024/savitribaiphulepune.html")
    elif int(year) == 2022 and location == "allsaintscollege":
        return render(request, 'conference/annualConference/2022/allsaintssollege.html')
    elif int(year) == 2022 and location == "louisianatechuniversity":
        return render(request, 'conference/annualConference/2022/louisiana-tech-university.html')
    elif int(year) == 2022 and location == "louisianastageuniversitysherveport":
        return render(request, 'conference/annualConference/2022/louisianastateuniversityshreveport.html')
    elif int(year) == 2022 and location == "louisianatechuniversitymonroe":
        return render(request, 'conference/annualConference/2022/universityofLouisianaMonroe.html')
    elif int(year) == 2022 and location == "donboscocollegechennai":
        return render(request, 'conference/annualConference/2022/donbosco-college.html')
    elif int(year) == 2021 and location == "jyotinivascollegeautonompus":
        return render(request, 'conference/annualConference/2021/jncaB.html')
    elif int(year) == 2021 and location == "binghamtonuniversity2021":
        return render(request, 'conference/annualConference/2021/binghamton-university.html')
    elif int(year) == 2020 and location == "christuniversitytvm":
        return render(request, 'conference/annualConference/2020/christuniversitytrivandrum.html')
    elif int(year) == 2019 and location == "christuniversity":
        return render(request, 'conference/annualConference/2019/christ-university-bangalore.html')
    elif int(year) == 2019 and location == "stannesdegreecollege":
        return render(request, 'conference/annualConference/2019/stannes-college.html')


def yclpCourse(request):
    return render(request, 'courses/yclpCourse.html')


def dreams(request, drm):


    if drm == 'band':
        breadcrumbs= [
    {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
    {'name': 'PRODUCTIONS', 'url': None, 'icon': 'fas fa-film', 'active': False},
    {'name': 'Dreams Band', 'url': None, 'icon': 'fas fa-music', 'active': True}
]

        return render(request, 'productions/dreamsBand.html', {'drm': drm,'breadcrumbs': breadcrumbs})
    else:
        breadcrumbs= [
    {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
    {'name': 'DREAMS', 'url': None, 'icon': 'fas fa-star', 'active': False},
    {'name': 'DREAMS Program', 'url': None, 'icon': 'fas fa-rocket', 'active': True}
]
        return render(request, 'dreams/dreamsProgram.html', {'drm': drm, 'breadcrumbs': breadcrumbs})


def locations(request, loc):
    context = locations_data.get(loc)  
    return render(request, 'location/location.html',context)
    

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
            name=name,
            email=email,
            phone=phone,
            interest=inter,
            user_type=utype,
            st_addr=staddr,
            # st_phone = stphone ,
            st_grade=stgrade,
            st_Pname=ptname,
            st_Pnum=ptphone,
            st_Pemail=ptemail,
            st_Paddr=ptaddr,
            vl_type=volt,
            vl_about=intro,
            vl_expert=expertise,
            # vl_phone = vlphone ,
            ptr_addr=partaddr,
            # ptr_phone= partphone ,
            ptr_msg=partmsg)
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
    confreg = ConferenceRegistration.objects.filter(
        user_type='Paticipant').all()
    # confreg = ConferenceRegistration.objects.all()

    print(confreg)
    writer = csv.writer(response)

    writer.writerow(['Date', 'Name', 'Email ID', 'Phone No', 'Interest', 'Student Address',
                     'Student Grade', 'Parent Name', 'Parent Mobile', 'Parent Email ID',
                     'Parent Address', 'User Type'])
    for i in confreg:
        writer.writerow([i.date, i.name, i.email, i.phone, i.interest, i.st_addr, i.st_grade,
                         i.st_Pname, i.st_Pnum, i.st_Pemail, i.st_Paddr, i.user_type])
    return response


def downloadvoltcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vounteer_list.csv"'
    confreg = ConferenceRegistration.objects.filter(
        user_type='Volunteer').all()

    writer = csv.writer(response)

    writer.writerow(['Date', 'Name', 'Email ID', 'Phone No', 'Interest', 'Volunteer Type',
                     'Intro', 'Areas of expertise', 'User Type'])
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
        writer.writerow([i.date, i.name, i.email, i.phone,
                         i.interest, i.ptr_addr, i.ptr_msg, i.user_type])
    return response


def testimonials(request):
    # Convert date strings to datetime objects
    for testimonial in TESTIMONIALS_DATA:
        if isinstance(testimonial["date"], str):
            testimonial["date"] = datetime.strptime(testimonial["date"], "%Y-%m-%d").date()

    context = {
        'testimonials': TESTIMONIALS_DATA
    }
    return render(request, 'home/view_testimonials.html', context)


def sustainability(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Sustainability', 'url': None, 'icon': 'fas fa-leaf', 'active': True}
    ]

    return render(request, 'aboutUs/sustainability.html', {'breadcrumbs': breadcrumbs})



def llfp(request):
    return render(request, 'courses/llfp2024.html', {'data': llfp_2024})

def contactUs(request):
    breadcrumbs = [
        {'name': 'Home', 'url': 'main', 'icon': 'fas fa-home', 'active': False},
        {'name': 'About Us', 'url': None, 'icon': 'fas fa-info-circle', 'active': False},
        {'name': 'Contact Us', 'url': None, 'icon': 'fas fa-address-book', 'active': True}
    ]
    return render(request, 'aboutUs/contactus.html', {'breadcrumbs': breadcrumbs})

# CLUB Pages

def club_overview(request):
    return render(request, 'clubs/overview.html')


def community_club(request):
    return render(request, 'clubs/community.html')


def conversation_club(request):
    return render(request, 'clubs/conversation.html')


def professional_club(request):
    return render(request, 'clubs/professional.html')


def growandglow_club(request):
    return render(request, 'clubs/selfhelp.html')


def youthleadership_club(request):
    return render(request, 'clubs/youthleadership.html')

def error_pages(request, exception=None):
    data = {}
    return render(request, 'home/errorpage.html', data)

def news_letter_html(request,month,year):
    if month == 'december' and year == '2024':
        context = {
            'month': month,
            'year': year,
        }
        return render(request, 'newsletters/'+month+'-'+year+'.html',context)
    else:
        return redirect('main')
    

def human(request):
    return render(request, 'productions/human.html')

def annual_report(request):
    return render(request, 'newsletters/annual_report.html')