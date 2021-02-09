from django.contrib import admin
from django.urls import path
from calender.views import index, event, receive
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event',event),
    path('receive',receive),
    path('',index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

