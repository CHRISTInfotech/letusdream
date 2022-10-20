from django.contrib import admin
from django.urls import path, include

from home.views import bangalorechristuniversity, donboscocollege, stannescollege, loyola, binghamtonUniversity, calender, downloadcsv, index, locations, aboutUs, louisianatechuniversity, media, aboutConference, newsletter, pressRelease, photoGallery,  registration_user, trriennialConference,  cuT, jncaB, dreams, annualConference, yclpCourse, research, publications, testimonials

urlpatterns = [
    path('', index, name='main'),
    path('locations/<str:loc>', locations, name='locations'),
    path('about-us', aboutUs, name='about-us'),
    path('media', media, name='media'),
    path('newsletter', newsletter, name='newsletter'),
    path('press-release/', pressRelease, name="press-release"),
    path('photo-gallery/', photoGallery, name="photo-gallery"),
    path('about-conference', aboutConference, name='about-conference'),
    path('annual-conference', annualConference, name='annual-conference'),
    path('trriennial-conference', trriennialConference,
         name='trriennial-conference'),
    path('yclpCourse', yclpCourse, name='yclp-course'),
    path('research', research, name='research'),
    path('publications', publications, name='publications'),
    path('christ-university-bangalore', bangalorechristuniversity,
         name='christ-university-bangalore'),
    path('binghamton-university-new-york', binghamtonUniversity,
         name='binghamton-university-new-york'),
    path('christ-university-thiruvananthapuram', cuT,
         name='christ-university-thiruvananthapuram'),
    path('jyoti-nivas-college-autonomous', jncaB,
         name='jyoti-nivas-college-autonomous'),
    path('louisiana-tech-university', louisianatechuniversity,
         name='louisiana-tech-university'),
    path('donboscocollege',donboscocollege,name='donboscocollege'),
    path('loyola',loyola,name='loyola'),
    path('stannescollege',stannescollege,name='stannescollege'),
    path('dreams/<str:drm>', dreams, name='dreams'),
    path('locations/<str:loc>', locations, name='locations'),
    path('registration_user', registration_user, name='registration_user'),
    path('calender', calender, name='calender'),
    path('downloadcsv', downloadcsv, name='downloadcsv'),
    path('testimonials',testimonials,name='testimonials'),
    
]
