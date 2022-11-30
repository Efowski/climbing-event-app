from logging import PlaceHolder
from django import forms
from django.forms import  ModelForm
from django.contrib.auth.models import User
 

from .models import Event

class EventForm(ModelForm):

    class Meta:
        model = Event

        fields =  ('name', 'venue', 'event_date', 'description', 'participants', 'event_poster')

        labels = {
            'name': 'Name',
            'venue': 'Venue',
            'event_date': 'Event Date',
             
            'description': 'Description',
            'participant': 'Participant',
            'event_poster': 'Event Poster',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name' }),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Event Place' }),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'administrator': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Administrator'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event description'}),
            'participant': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Participants'}),
            'event_poster': forms.ImageField()
        }


class UserForm(ModelForm):

    class Meta:
        model = User

        fields = ('username',   'first_name', 'last_name')

        labels = {
            'username': 'Username',
            
            'first_name': 'First Name',
            'last_name': 'Last Name',

        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username' }),
             
            
             
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), 
             
        }