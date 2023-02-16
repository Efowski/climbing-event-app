from logging import PlaceHolder
from django import forms
from django.forms import  ModelForm
from django.contrib.auth.models import User

from .models import Venue 
from .models import Event
from .models import Comment


class EventForm(ModelForm):

    class Meta:
        model = Event

        fields =  ('name', 'venue', 'event_date', 'description', 'participants','event_poster' )

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
            
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue

        fields = ('name', 'address', 'zipcode', 'website', 'email_address', 'venue_image')

        labels = {
            'name': 'Name Venue', 
            'address': 'Address',
            'zipcode': 'Zipcode',
            'website': 'Website',
            'email_address': 'Email Address',
            'venue_image': '',
             
            
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Address'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E mail'}),
            
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


class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ('contents', )

        labels = {
            # 'author': 'Author',
            'contents': 'Write Comment',
        }

        widgets =  {
            'contents': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your Comment'}),
            
        }