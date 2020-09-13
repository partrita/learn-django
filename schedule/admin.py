from django.contrib import admin
from .models import Event, Equipment, Manager

admin.site.register(Manager)
admin.site.register(Event)
admin.site.register(Equipment)
