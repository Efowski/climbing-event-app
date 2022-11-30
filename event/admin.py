from django.contrib import admin

from event.models import Event, ClimbUser, Venue


admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(ClimbUser)