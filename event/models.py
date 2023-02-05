
from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse




class ClimbUser(models.Model):
    username = models.CharField(max_length=50, default="Username")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User Email' )

    def __str__(self):
        return self.username


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Venue(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zipcode = models.CharField('ZIPCODE', max_length=15)
    website = models.URLField('Webiste', blank=True)
    email_address = models.EmailField('Email Address', blank=True, unique=True)
    venue_image = models.ImageField(upload_to='venue_image/', null=True, blank=True,)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    name = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    event_date = models.DateTimeField('Event Date')
    administrator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE )
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(User, blank=True, related_name='events' )
    event_poster = models.ImageField(upload_to='poster/', null=True, blank=True,)
    slug = models.SlugField(null=True, unique=True)


    def __str__(self):
        return self.name            
        

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.self})
    