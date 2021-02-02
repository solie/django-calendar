from django.db import models


class Doctor(models.Model):
    doctor_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    display_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=32)
    zoom_meeting_id = models.CharField(max_length=64, blank=True, null=True)
    chat_room_url = models.URLField(max_length=200, blank=True, null=True)
    chat_room_line_id = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='doctor', blank=True, null=True)
    verified = models.BooleanField(default=False, blank=True, null=True)
    timezone = models.CharField(max_length=20, default='zh-tw')
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        editable=True)

    def __str__(self):
        return "{}_{}".format(self.doctor_id, self.display_name)


class Event(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    recurring = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.doctor}_{self.start_time}_{self.end_time}"
