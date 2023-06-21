from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .form import EventForm, UserForm, VenueForm, CommentForm
from .models import Event, Venue, Comment
from django.db.models import Q 


def home(request):
    all_events = Event.objects.all().order_by('event_date')

    return render(request, 'home.html', {'all_events':all_events, })


def all_events(request):
     
    events = Event.objects.all()

    return render(request, 'events_list.html', {'events': events, })


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


def event_details(request, slug):
    user = User()
    event = Event.objects.get(slug=slug)
    commentform = CommentForm()
    
    if request.method == 'POST':
        commentform = CommentForm(request.POST or None)
        if commentform.is_valid:
            content = request.POST.get('contents')
            parent_object = None
            try:
                parent_id = int(request.POST.get('parent_id') )
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)    
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_object = parent_qs.first()
            comment = Comment.objects.create(event=event, author=request.user, contents=content, parent=parent_object)
            
            comment.save()
            messages.success(request, "You have added a comment")
            return redirect('event-details', slug=slug)
        else:
            commentform = CommentForm()
    
    comments = Comment.objects.all().order_by('-date_added')
             
    return render(request, 'event_details.html', {'event': event, 'user': user, 'commentform': commentform, 'comments':comments  })


@login_required
def event_update(request, slug):
    event = Event.objects.get(slug=slug)
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

"""To do search event and venue with few icontains"""
def search_event(request):
    
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Event.objects.filter(Q(name__icontains=searched) & Q(description__icontains=searched))
        

        return render(request, 'event_search.html', {'events': events, 'searched': searched, })
    else:
        print ("Event not found")
        return render(request, 'event_search.html', { })


def register_event(request, event_id):
    
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        event.participants.add(request.user)
        messages.success(request, "You have successfully registered for the event")
        return redirect('home')

    return render (request, 'register_event.html', {'event': event,  })


# Venue CRUD


def venues_list(request):
    venue = Venue.objects.all()

    return render(request, 'venue_list.html', {'venue': venue })

def events_venue(request,  slug):
    venue = Venue.objects.get(slug=slug)

    events = venue.event_set.all()

    if events:
        return render(request, 'venue_events.html', {'events': events})

    else:
        messages.success(request, "No Event in that Venue")
        return render(request, 'venue_events.html',)


@login_required
def create_venue(request):
    submit = False
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = VenueForm(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/create_venue?submit=True')
            else:
                messages.success(request, 'Fields contain errors')
        else: 
            form = VenueForm()
            return render (request, 'create_venue.html', {'form': form,})    
        
    return render (request, 'create_venue.html', {'form': form,}) 


def venue_details(request, slug):
    venue = Venue.objects.get(slug=slug)

    venue_events = venue.event_set.all()



    return render (request, 'venue_details.html', {'venue': venue, 'venue_events': venue_events })
         

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
def delete_user_account(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success('Your account was delete')
    return render(request, 'home')



 