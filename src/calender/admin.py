from django.contrib import admin
from calender.models import Doctor, Event


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
        'email',
        'description',
        'timezone',
        'zoom_meeting_id',
        'chat_room_line_id',
        'chat_room_url',
        'verified')
    search_fields = list_display


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_time', 'end_time', 'recurring')
    search_fields = list_display
