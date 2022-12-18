 
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Event, Venue
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .form import EventForm, UserForm

 


def home(request):
    all_events = Event.objects.all()

    return render(request, 'home.html', {'all_events':all_events, })


@login_required
def create_event(request):
    submit = False
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/create_event?submit=True')
            else:
                messages.success(request, 'Fields contain errors')
        else: 
            form = EventForm()
            return render (request, 'create_event.html', {'form': form,})    
    else:
        messages.error(request, "You must create account to create Event")
    
def event_details(request, event_id):
    user = User()

    event = Event.objects.get(pk=event_id)
    return render(request, 'event_details.html', {'event': event, 'user': user,})

@login_required
def event_update(request, event_id):
    event = Event.objects.get(pk=event_id)
    event_form = EventForm(request.POST or None, instance=event) 
    if request.user == event.administrator:

        if event_form.is_valid():
            
            event_form.save() 
            messages.success(request, "Event was updated succesfully")
            return redirect('home' )
        
        return render(request, 'event_update.html', {'event_form': event_form, 'event': event,})
    else:
        messages.success(request, "You're not administrate this event")
        return redirect('event-details')

@login_required
def event_delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.administrator:

        event.delete()
        return redirect('home' )
    else:
        messages.success(request, "You're not administrator this Event")
        return redirect('home')


def search_event(request):
    
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Event.objects.filter(description__contains=searched)
        

        return render(request, 'event_search.html', {'events': events, 'searched': searched, })
    else:
        return render(request, 'event_search.html', { })


def register_event(request, event_id):
    
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        event.participants.add(request.user)
        messages.success(request, "You have successfully registered for the event")
        return redirect('home')

    return render (request, 'register_event.html', {'event': event,  })


# Venue 

def venue_list(request):
    all_venue = Venue.objects.all()
    
    return render(request, 'venue_list.html', {'all_venue': all_venue,})


def events_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)

    events = venue.event_set.all()

    if events:
        return render(request, 'venue_events.html', {'evetns': events})

    else:
        messages.success(request, "No Event in that Venue")
        return render(request, 'venue_events.html',)

# User and User Profile



@login_required(login_url='login')
def user_profile(request, id):
    user = User.objects.get(id=id)
    user_form = UserForm(instance=user)

    events = Event.objects.filter(participants=request.user)
    
    return render(request, 'user_profile.html', {'user': user, 'user_form': user_form, 'events': events,   })

@login_required
def update_profile(request, id):
    user = User.objects.get(id=id)
    user_form = UserForm(request.POST or None, instance=request.user)

    if request.method == 'POST':
       if  user_form.is_valid():

            user_form.save()
            messages.success(request, "Profile was updated succesfully")
            return redirect('home')



    return render(request, 'update_profile.html', {'user': user, 'user_form': user_form,})

@login_required
def delete_profil(request, id):
    pass