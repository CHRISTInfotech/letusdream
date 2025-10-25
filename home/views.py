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
        "page_title": "Home",
    }
    return render(request, "home/index.html")


def aboutUs(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {"name": "Overview", "url": None, "icon": "fas fa-eye", "active": True},
    ]
    return render(request, "aboutUs/aboutUs.html", {"breadcrumbs": breadcrumbs})


def leadership(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {"name": "Leadership", "url": None, "icon": "fas fa-user-tie", "active": True},
    ]
    return render(request, "aboutUs/leadership.html", {"breadcrumbs": breadcrumbs})


def login(request):
    if request.method == "POST" and request.user.is_authenticated:
        return render(request, "AdminPanel/home.html")


def media(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {"name": "Media", "url": None, "icon": "fas fa-photo-video", "active": True},
    ]

    return render(request, "aboutUs/media.html", {"breadcrumbs": breadcrumbs})


def events(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {"name": "Events", "url": None, "icon": "fas fa-calendar-days", "active": True},
    ]

    return render(request, "aboutUs/events.html", {"breadcrumbs": breadcrumbs})


def pressRelease(request):
    press_items = [
        {
            "date": "Feb 10, 2025",
            "image": "Aboutus/Media/Press/Press10.jpg",
            "alt": "Press 10",
            "link": "Aboutus/Media/Press/Press10.jpg",
        },
        {
            "date": "Dec 2024",
            "image": "Aboutus/Media/Press/lud news.png",
            "alt": "LUD News December 2024",
            "link": "2024/Conference/news/ConversationsToday-December2024.pdf",
        },
        {
            "date": "Jul 25, 2015",
            "image": "Aboutus/Media/Press/Press2.jpg",
            "alt": "Press 2",
            "link": "Aboutus/Media/Press/Press2.jpg",
        },
        {
            "date": "Jul 27, 2016",
            "image": "Aboutus/Media/Press/Press3.jpg",
            "alt": "Press 3",
            "link": "Aboutus/Media/Press/Press3.jpg",
        },
        {
            "date": "Jul 27, 2016",
            "image": "Aboutus/Media/Press/Press6.jpg",
            "alt": "Press 6",
            "link": "Aboutus/Media/Press/Press6.jpg",
        },
        {
            "date": "Nov 02, 2017",
            "image": "Aboutus/Media/Press/Press7.png",
            "alt": "Press 7",
            "link": "Aboutus/Media/Press/Press7.png",
        },
        {
            "date": "Nov 02, 2017",
            "image": "Aboutus/Media/Press/Press8.png",
            "alt": "Press 8",
            "link": "Aboutus/Media/Press/Press8.png",
        },
        {
            "date": "Jul 25, 2018",
            "image": "Aboutus/Media/Press/Press5.jpeg",
            "alt": "Press 5",
            "link": "Aboutus/Media/Press/Press5.jpeg",
        },
        {
            "date": "",
            "image": "Aboutus/Media/Press/Press1.jpg",
            "alt": "Press 1",
            "link": "Aboutus/Media/Press/Press1.jpg",
        },
        {
            "date": "",
            "image": "Aboutus/Media/Press/Press4.jpeg",
            "alt": "Press 4",
            "link": "Aboutus/Media/Press/Press4.jpeg",
        },
    ]
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {
            "name": "Media",
            "url": "media",
            "icon": "fas fa-photo-video",
            "active": False,
        },
        {
            "name": "Press Release",
            "url": None,
            "icon": "fas fa-newspaper",
            "active": True,
        },
    ]
    return render(
        request,
        "aboutUs/pressRelease.html",
        {"breadcrumbs": breadcrumbs, "press_items": press_items},
    )


def newsletter(request):
    newsletters = [
        {
            "pdf_url": "2025/newsletter/NewsBulletin_Changanassery.pdf",
            "image_url": "2025/newsletter/NewsBulletin_Changanassery.png",
            "title": "News Bulletin Changanassery",
            "month": "Jan",
            "day": "15",
            "year": "2025",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/dec2024.png",  # image is same as pdf here
            "image_url": "Aboutus/Media/Newsletter/dec2024.png",
            "title": "December 2024 Newsletter",
            "month": "Jul",
            "day": "",
            "year": "2024",
            "is_url": True,
            "url_name": "newsletter-page",
            "url_args": ["december", "2024"],
        },
        {
            "pdf_url": "2024/newsletters/DREAMSJNC2024Newsletter.pdf",
            "image_url": "2024/newsletters/thumbnails/dreamsjnc24.png",
            "title": "Dreams JNC 2024",
            "month": "Jul",
            "day": "",
            "year": "2024",
        },
        {
            "pdf_url": "2024/newsletters/DREAMSxKJCMTNewsletter_1.pdf",
            "image_url": "2024/newsletters/thumbnails/DREAMSxKJCMTNewsletter_1.png",
            "title": "Dreams x KJCMT Newsletter 1",
            "month": "Jul",
            "day": "",
            "year": "2024",
        },
        {
            "pdf_url": "2024/newsletters/Changanassery_2.pdf",
            "image_url": "2024/newsletters/thumbnails/Changanassery_2.png",
            "title": "Changanassery 2",
            "month": "Jul",
            "day": "",
            "year": "2024",
        },
        {
            "pdf_url": "2024/newsletters/Changanassery_1.pdf",
            "image_url": "2024/newsletters/thumbnails/Changanassery_1.png",
            "title": "Changanassery 1",
            "month": "Jul",
            "day": "",
            "year": "2024",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/LUD Connect 01 - September 2023.pdf",
            "image_url": "Aboutus/Media/Newsletter/LUD Connect 01 - September 2023.png",
            "title": "LUD Connect 01",
            "month": "Sep",
            "day": "",
            "year": "2023",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/LUD Connect 02 - September 2023.pdf",
            "image_url": "Aboutus/Media/Newsletter/LUD Connect 02 - September 2023.png",
            "title": "LUD Connect 02",
            "month": "Sep",
            "day": "",
            "year": "2023",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/LUD Connect 03 - October 2023.pdf",
            "image_url": "Aboutus/Media/Newsletter/LUD Connect 03 - October 2023.png",
            "title": "LUD Connect 03",
            "month": "Oct",
            "day": "",
            "year": "2023",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-1.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-1.jpg",
            "title": "Newsletter 1",
            "month": "Aug",
            "day": "27",
            "year": "2020",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-2.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-2.jpg",
            "title": "Newsletter 2",
            "month": "Oct",
            "day": "21",
            "year": "2020",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-3.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-3.jpg",
            "title": "Newsletter 3",
            "month": "Nov",
            "day": "10",
            "year": "2020",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-4.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-4.jpg",
            "title": "Newsletter 4",
            "month": "Nov",
            "day": "22",
            "year": "2020",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-5.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-5.jpg",
            "title": "Newsletter 5",
            "month": "Nov",
            "day": "22",
            "year": "2020",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-6.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-6.jpg",
            "title": "Newsletter 6",
            "month": "Nov",
            "day": "22",
            "year": "2020",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-7.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-7.jpg",
            "title": "Newsletter 7",
            "month": "Jun",
            "day": "03",
            "year": "2021",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-8.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-8.jpg",
            "title": "Newsletter 8",
            "month": "Oct",
            "day": "03",
            "year": "2021",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-9.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-9.jpg",
            "title": "Newsletter 9",
            "month": "Dec",
            "day": "03",
            "year": "2021",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Lead_team.pdf",
            "image_url": "Aboutus/Media/Newsletter/lead_team.png",
            "title": "Lead Team",
            "month": "June",
            "day": "03",
            "year": "2023",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/Newsletter-10.jpg",
            "image_url": "Aboutus/Media/Newsletter/Newsletter-10.jpg",
            "title": "Newsletter 10",
            "month": "May",
            "day": "13",
            "year": "2017",
        },
        {
            "pdf_url": "Aboutus/Media/Newsletter/studentExchangeProgram.jpg",
            "image_url": "Aboutus/Media/Newsletter/studentExchangeProgram.jpg",
            "title": "Student Exchange Program",
            "month": "June",
            "day": "01",
            "year": "2024",
        },
    ]
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {
            "name": "Media",
            "url": "media",
            "icon": "fas fa-photo-video",
            "active": False,
        },
        {"name": "Newsletter", "url": None, "icon": "fas fa-envelope", "active": True},
    ]

    # Sort newsletters by year and month
    newsletters.sort(key=lambda x: (x["year"], x["month"]), reverse=True)
    # Render the template with the newsletters and breadcrumbs
    return render(
        request,
        "aboutUs/newsletter.html",
        {"breadcrumbs": breadcrumbs, "newsletters": newsletters},
    )


def photoGallery(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {
            "name": "Media",
            "url": "media",
            "icon": "fas fa-photo-video",
            "active": False,
        },
        {"name": "Photo Gallery", "url": None, "icon": "fas fa-image", "active": True},
    ]
    return render(request, "aboutUs/photo-gallery.html", {"breadcrumbs": breadcrumbs})


def youtubeMedia(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {
            "name": "Media",
            "url": "media",
            "icon": "fas fa-photo-video",
            "active": False,
        },
        {
            "name": "YouTube Media",
            "url": None,
            "icon": "fab fa-youtube",
            "active": True,
        },
    ]
    return render(request, "aboutUs/media-yt.html", {"breadcrumbs": breadcrumbs})


def aboutConference(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Conference", "url": None, "icon": "fas fa-calendar", "active": False},
        {
            "name": "About Conference",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": True,
        },
    ]
    return render(
        request, "conference/aboutConference.html", {"breadcrumbs": breadcrumbs}
    )


def allConferences(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Conference", "url": None, "icon": "fas fa-calendar", "active": False},
        {
            "name": "Annual Conferences",
            "url": None,
            "icon": "fas fa-calendar-alt",
            "active": True,
        },
    ]
    return render(
        request, "conference/annualConference.html", {"breadcrumbs": breadcrumbs}
    )


def triennialConference(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "Conference",
            "url": "Conferences",
            "icon": "fas fa-calendar",
            "active": False,
        },
        {
            "name": "Triennial Conferences",
            "url": None,
            "icon": "fas fa-calendar-alt",
            "active": True,
        },
    ]
    return render(
        request,
        "conference/triennialConference.html",
        {
            "breadcrumbs": breadcrumbs,
        },
    )


def triennialConference2020(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "Conferences",
            "url": None,
            "icon": "fas fa-calendar-alt",
            "active": False,
        },
        {
            "name": "Triennial Conferences",
            "url": "trriennial-conference",
            "icon": "fas fa-calendar-check",
            "active": False,
        },
        {
            "name": "2020 Conference",
            "url": None,
            "icon": "fas fa-file-alt",
            "active": True,
        },
    ]

    return render(
        request,
        "conference/triennialConference/triennialConference2020.html",
        {
            "breadcrumbs": breadcrumbs,
        },
    )


def triennialConference2023(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "Conferences",
            "url": None,
            "icon": "fas fa-calendar-alt",
            "active": False,
        },
        {
            "name": "Triennial Conferences",
            "url": "trriennial-conference",
            "icon": "fas fa-calendar-check",
            "active": False,
        },
        {"name": "2023", "url": None, "icon": "fas fa-file-alt", "active": True},
    ]

    context = {
        "bgcolor": "#274C7D",
        "conference_data": CONFERENCE_DATA,
        "breadcrumbs": breadcrumbs,
    }
    return render(
        request, "conference/triennialConference/triennialConference2023.html", context
    )


def howtoConference(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "Conference",
            "url": None,
            "icon": "fas fa-calendar-alt",
            "active": False,
        },
        {
            "name": "Conference Resources",
            "url": None,
            "icon": "fas fa-box-open",
            "active": True,
        },
    ]
    return render(
        request,
        "conference/ludConferences.html",
        {
            "breadcrumbs": breadcrumbs,
        },
    )


def annualConferences(request, year, location):
    if int(year) == 2024 and location == "stfrancisdesalescollege":
        return render(
            request, "conference/annualConference/2024/stfrancisdesalescollege.html"
        )
    elif int(year) == 2024 and location == "womenschristiancollege":
        return render(
            request, "conference/annualConference/2024/womenschristiancollege.html"
        )
    elif int(year) == 2024 and location == "gramblingstateuniversity":
        return render(
            request, "conference/annualConference/2024/gamblingstateuniversity.html"
        )
    elif int(year) == 2024 and location == "binghamtonuniversity2024":
        return render(
            request, "conference/annualConference/2024/binghamtonuniversity2024.html"
        )
    elif int(year) == 2024 and location == "christnagarcollege":
        return render(
            request, "conference/annualConference/2024/christnagarcollege.html"
        )
    elif int(year) == 2024 and location == "stfrancisdegreecollege":
        return render(
            request, "conference/annualConference/2024/stfrancisdegreecollege.html"
        )
    elif int(year) == 2024 and location == "savitribaiphulepune":
        return render(
            request, "conference/annualConference/2024/savitribaiphulepune.html"
        )
    elif int(year) == 2022 and location == "allsaintscollege":
        return render(request, "conference/annualConference/2022/allsaintssollege.html")
    elif int(year) == 2022 and location == "louisianatechuniversity":
        return render(
            request, "conference/annualConference/2022/louisiana-tech-university.html"
        )
    elif int(year) == 2022 and location == "louisianastageuniversitysherveport":
        return render(
            request,
            "conference/annualConference/2022/louisianastateuniversityshreveport.html",
        )
    elif int(year) == 2022 and location == "louisianatechuniversitymonroe":
        return render(
            request, "conference/annualConference/2022/universityofLouisianaMonroe.html"
        )
    elif int(year) == 2022 and location == "donboscocollegechennai":
        return render(request, "conference/annualConference/2022/donbosco-college.html")
    elif int(year) == 2021 and location == "jyotinivascollegeautonompus":
        return render(request, "conference/annualConference/2021/jncaB.html")
    elif int(year) == 2021 and location == "binghamtonuniversity2021":
        return render(
            request, "conference/annualConference/2021/binghamton-university.html"
        )
    elif int(year) == 2020 and location == "christuniversitytvm":
        return render(
            request, "conference/annualConference/2020/christuniversitytrivandrum.html"
        )
    elif int(year) == 2019 and location == "christuniversity":
        return render(
            request, "conference/annualConference/2019/christ-university-bangalore.html"
        )
    elif int(year) == 2019 and location == "stannesdegreecollege":
        return render(request, "conference/annualConference/2019/stannes-college.html")


def yclpCourse(request):
    return render(request, "courses/yclpCourse.html")


def dreams(request, drm):

    if drm == "band":
        breadcrumbs = [
            {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
            {
                "name": "PRODUCTIONS",
                "url": None,
                "icon": "fas fa-film",
                "active": False,
            },
            {
                "name": "Dreams Band",
                "url": None,
                "icon": "fas fa-music",
                "active": True,
            },
        ]

        return render(
            request,
            "productions/dreamsBand.html",
            {"drm": drm, "breadcrumbs": breadcrumbs},
        )
    else:
        breadcrumbs = [
            {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
            {"name": "DREAMS", "url": None, "icon": "fas fa-star", "active": False},
            {
                "name": "DREAMS Program",
                "url": None,
                "icon": "fas fa-rocket",
                "active": True,
            },
        ]
        return render(
            request,
            "dreams/dreamsProgram.html",
            {"drm": drm, "breadcrumbs": breadcrumbs},
        )


def locations(request, loc):
    context = locations_data.get(loc)
    return render(request, "location/location.html", context)


def research(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Research", "url": "research", "icon": "fa-solid fa-book", "active": False},
    ]
    return render(request, "research/research.html",{"breadcrumbs": breadcrumbs})


def publications(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Research", "url": "research", "icon": "fa-solid fa-book", "active": False},
        {
            "name": "Publications",
            "url": None,
            "icon": "fa-solid fa-file-import",
            "active": True,
        },
    ]
    return render(
        request, "research/publications.html", {"breadcrumbs": breadcrumbs}
    )


def calender(request):
    return render(request, "home/calender.html")


def testimonials(request):
    # Convert date strings to datetime objects
    for testimonial in TESTIMONIALS_DATA:
        if isinstance(testimonial["date"], str):
            testimonial["date"] = datetime.strptime(
                testimonial["date"], "%Y-%m-%d"
            ).date()

    context = {"testimonials": TESTIMONIALS_DATA}
    return render(request, "home/view_testimonials.html", context)


def sustainability(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {"name": "Sustainability", "url": None, "icon": "fas fa-leaf", "active": True},
    ]

    return render(request, "aboutUs/sustainability.html", {"breadcrumbs": breadcrumbs})


def llfp(request):
    return render(request, "courses/llfp2024.html", {"data": llfp_2024})


def contactUs(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {
            "name": "About Us",
            "url": None,
            "icon": "fas fa-info-circle",
            "active": False,
        },
        {
            "name": "Contact Us",
            "url": None,
            "icon": "fas fa-address-book",
            "active": True,
        },
    ]
    return render(request, "aboutUs/contactus.html", {"breadcrumbs": breadcrumbs})


# CLUB Pages


def club_overview(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Clubs", "url": "club-overview", "icon": "fa-solid fa-cubes-stacked", "active": True},
    ]
    return render(request, "clubs/overview.html", {"breadcrumbs": breadcrumbs})


def community_club(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Clubs", "url": "club-overview", "icon": "fa-solid fa-cubes-stacked", "active": False},
        {"name": "Community Hubs", "url": "community-club", "icon": "fa-solid fa-people-arrows", "active": True},
    ]
    return render(request, "clubs/community.html", {"breadcrumbs": breadcrumbs})


def conversation_club(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Clubs", "url": "club-overview", "icon": "fa-solid fa-cubes-stacked", "active": False},
        {"name": "Conversation Club", "url": "conversation-club", "icon": "fa-solid fa-people-arrows", "active": True},
    ]
    return render(request, "clubs/conversation.html", {"breadcrumbs": breadcrumbs})


def professional_club(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Clubs", "url": "club-overview", "icon": "fa-solid fa-cubes-stacked", "active": False},
        {"name": "Professional Club", "url": "professional-club", "icon": "fa-solid fa-people-arrows", "active": True},
    ]
    return render(request, "clubs/professional.html", {"breadcrumbs": breadcrumbs})


def growandglow_club(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Clubs", "url": "club-overview", "icon": "fa-solid fa-cubes-stacked", "active": False},
        {"name": "Grow and Glow Club", "url": "growandglow-club", "icon": "fa-solid fa-people-arrows", "active": True},
    ]
    return render(request, "clubs/selfhelp.html", {"breadcrumbs": breadcrumbs})


def youthleadership_club(request):
    breadcrumbs = [
        {"name": "Home", "url": "main", "icon": "fas fa-home", "active": False},
        {"name": "Clubs", "url": "club-overview", "icon": "fa-solid fa-cubes-stacked", "active": False},
        {"name": "Global Youth Leadership Network", "url": "youthleadership-club", "icon": "fa-solid fa-people-arrows", "active": True},
    ]
    return render(request, "clubs/youthleadership.html", {"breadcrumbs": breadcrumbs})


def error_pages(request, exception=None):
    data = {}
    return render(request, "home/errorpage.html", data)


def news_letter_html(request, month, year):
    if month == "december" and year == "2024":
        context = {
            "month": month,
            "year": year,
        }
        return render(request, "newsletters/" + month + "-" + year + ".html", context)
    else:
        return redirect("main")


def human(request):
    return render(request, "productions/human.html")


def annual_report(request):
    return render(request, "newsletters/annual_report.html")


def conclave(request):
    return render(request, "conference/conclave.html")
