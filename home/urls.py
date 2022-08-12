from django.contrib import admin
from django.urls import path, include

from home.views import index, locations, aboutUs, media, aboutConference, trriennialConference, buNY, cuB, cuT, jncaB, \
    ltuLouisiana, dreams, annualConference, yclpCourse, research, publications

urlpatterns = [
    path('', index, name='main'),
    path('locations/<str:loc>', locations, name='locations'),
    path('about-us', aboutUs, name='about-us'),
    path('news', media, name='news'),
    path('about-conference', aboutConference, name='about-conference'),
    path('annual-conference', annualConference, name='annual-conference'),
    path('trriennial-conference', trriennialConference, name='trriennial-conference'),
    path('yclpCourse', yclpCourse, name='yclp-course'),
    path('research',research,name='research'),
    path('publications',publications,name='publications'),
    path('binghamton-university-new-york', buNY, name='binghamton-university-new-york'),
    path('christ-university-bangalore', cuB, name = 'christ-university-bangalore'),
    path('christ-university-thiruvananthapuram', cuT, name = 'christ-university-thiruvananthapuram'),
    path('jyoti-nivas-college-autonomous', jncaB, name = 'jyoti-nivas-college-autonomous'),
    path('louisiana-tech-university', ltuLouisiana, name = 'louisiana-tech-university'),
    path('dreams/<str:drm>', dreams, name='dreams'),
    path('locations/<str:loc>', locations, name='locations'),
]
