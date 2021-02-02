from django.contrib import admin
from django.urls import path
from calender.views import index, event, receive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event',event),
    path('receive',receive),
    path('',index),
]
