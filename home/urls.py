from django.contrib import admin
from django.urls import path, include

from home.views import index, locations, aboutUs, media, aboutConference, trriennialConference, buNY, cuB, cuT, jncaB, \
    ltuLouisiana, dreams, annualConference

urlpatterns = {
    path('', index, name='main'),
    path('location/<str:loc>', locations, name='locations'),
    path('about-us', aboutUs, name='about-us'),
    path('ltmedia', media, name='ltmedia'),
    path('about-conference', aboutConference, name='about-conference'),
    path('annual-conference', annualConference, name='annual-conference'),
    path('trriennial-conference', trriennialConference, name='trriennial-conference'),
    path('binghamton-university-new-york', buNY, name='binghamton-university-new-york'),
    path('christ-university-bangalore', cuB, name = 'christ-university-bangalore'),
    path('christ-university-thiruvananthapuram', cuT, name = 'christ-university-thiruvananthapuram'),
    path('jyoti-nivas-college-autonomous', jncaB, name = 'jyoti-nivas-college-autonomous'),
    path('louisiana-tech-university', ltuLouisiana, name = 'louisiana-tech-university'),
    path('dreams/<str:drm>', dreams, name='dreams'),
}
