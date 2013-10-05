from django.contrib import admin
from main.models import Event

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)
