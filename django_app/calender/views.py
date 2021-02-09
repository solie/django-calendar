from django.shortcuts import render
from django.conf import settings
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from calender.models import Event, Doctor
from datetime import datetime
import json


@csrf_exempt
def index(request):
    print(settings.VERSION)
    doctor = Doctor.objects.filter(verified=True)
    doctors = [{'id': item.doctor_id,
                'name': item.display_name,
                'color': item.color} for item in doctor]
    print(doctors)
    data = {'version': settings.VERSION, 'doctors': doctors}
    return render(request, 'index.html', data)


@csrf_exempt
def event(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        return JsonResponse({'msg': 'ok'})
    else:
        events = Event.objects.all()
        data = []
        for i in events:
            data.append({'title': i.doctor.display_name,
                         'start': i.start_time.strftime('%Y-%m-%dT%H:%M:00'),
                         'end': i.end_time.strftime('%Y-%m-%dT%H:%M:00'),
                         'color': i.doctor.color})
        return JsonResponse(data, safe=False)


@csrf_exempt
def receive(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        msg = f"Hello, {data['name']}"
        return JsonResponse({'msg': msg})
    else:
        return render(request, 'simple.html')


@csrf_exempt
def test_gc(request):
    print(request.headers)
    return JsonResponse(request.headers)
