from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('create_event', views.create_event, name='create-event'),
    path('event_details/<slug:slug>', views.event_details, name='event-details'),
    path('event_update/<slug:slug>', views.event_update, name='event-update'),
    path('event_delete/<slug:slug>', views.event_delete, name='event-delete'),
    path('events_list', views.all_events, name="events-list"),

    path('venues_list', views.venues_list, name="venues-list"),
    path('venue_events/<event_slug>', views.events_venue, name='events-venue'),
    path('create_venue', views.create_venue, name='create-venue'),
    path('venue_details/<slug:slug>', views.venue_details, name='venue-details'),
    
    
    #search any object e.g. event, user 
    path('search_event', views.search_event, name='search-event'),
    path('register_event/<slug:slug>', views.register_event, name='register-event'),

    #user profile
    path('user_profile/<id>', views.user_profile, name='user-profile'),
    path('update_profile/<id>', views.update_profile, name='update-profile'),
]