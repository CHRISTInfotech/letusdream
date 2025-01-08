from django.conf.urls import handler404, handler500, handler403, handler400
from django.urls import path

from .views import *

handler404 = 'home.views.error_pages'
handler500 = 'home.views.error_pages'
handler403 = 'home.views.error_pages' 
handler400 = 'home.views.error_pages' 

urlpatterns = [
    path('', index, name='main'),
    path('locations/<str:loc>', locations, name='locations'),
    path('about-us', aboutUs, name='about-us'),
    path('leadership', leadership, name='leadership'),
    path('media', media, name='media'),
    path('events', events, name='events'),
    path('newsletters', newsletter, name='newsletter'),
    path('press-release/', pressRelease, name="press-release"),
    path('photo-gallery/', photoGallery, name="photo-gallery"),
    path('youtube-media/', youtubeMedia, name="youtube-media"),
    path('dreams/<str:drm>', dreams, name='dreams'),
    path('locations/<str:loc>', locations, name='locations'),
    path('registration_user', registration_user, name='registration_user'),
    path('yclpCourse', yclpCourse, name='yclp-course'),
    path('research', research, name='research'),
    path('publications', publications, name='publications'),
    path('calender', calender, name='calender'),
    path('downloadcsv', downloadcsv, name='downloadcsv'),
    path('downloadvoltcsv', downloadvoltcsv, name='downloadvoltcsv'),
    path('downloadpartcsv', downloadpartcsv, name='downloadpartcsv'),
    path('testimonials', testimonials, name='testimonials'),
    path('sustainability', sustainability, name='sustainability'),
    path('llfp', llfp, name='llfp'),
    path('contactUs/', contactUs, name='conatctUs'),

    # CONFERENCE URLS
    path('conferences', aboutConference, name='Conferences'),
    path('annualConference', allConferences, name='annualConference'),
    path('trriennialConference', triennialConference, name='trriennial-conference'),
    path('triennial-conference-2020', triennialConference2020, name='tc-2020'),
    path('triennial-conference-2023', triennialConference2023, name='tc-2023'),
    path('run-lud-conference', howtoConference, name='run-lud-conference'),
    path('annualConference/<int:year>/<str:location>', annualConferences, name='annual-conference'),
    # CONFERENCE URLS ENDS

    # CLUB URLs
    path('clubs', club_overview, name='club-overview'),
    path('clubs/overview', club_overview, name='club-overview'),
    path('clubs/community', community_club, name='community-club'),
    path('clubs/conversation', conversation_club, name='conversation-club'),
    path('clubs/professional', professional_club, name='professional-club'),
    path('clubs/growandglow', growandglow_club, name='growandglow-club'),
    path('clubs/youth-leadership', youthleadership_club, name='youthleadership-club'),
    # CLUBS PAGES URL END
    
    path('newsletters/<str:month>/<str:year>',news_letter_html,name='newsletter-page'),

]
